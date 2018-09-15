#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.db import transaction
from user import decorators
from user.models import User
from cart.models import Cart
from .models import Order, OrderItem


@transaction.atomic()
@decorators.login_required
def order(request):
    if request.method == 'POST':
        transaction_id = transaction.savepoint()
        try:
            order = Order()
            order.user_id = request.session['user_id']
            order.total = float(request.POST['total_fee'])
            order.address = request.POST['address']
            order.save()
            cart_ids = [int(_) for _ in request.POST['cart_ids'].split(',')]
            for cart_id in cart_ids:
                order_item = OrderItem()
                order_item.order = order
                cart = Cart.objects.get(id=cart_id)
                item = cart.goods
                if item.in_stock >= cart.count:
                    item.in_stock = item.in_stock - cart.count
                    item.save()
                    # save item in order
                    order_item.item_id = item.id
                    order_item.price = item.price
                    order_item.count = cart.count
                    order_item.save()
                    # delete cart
                    cart.delete()
                else:
                    transaction.savepoint_rollback(transaction_id)
                    resp = HttpResponse(status=303)
                    resp['Location'] = reverse('cart:index')
                    return resp
        except Exception as e:
            print('==========%s' % e)
            transaction.savepoint_rollback(transaction_id)

        return redirect(reverse('user:order'))

    else:
        user = User.objects.get(id=request.session['user_id'])
        contact = user.contact_set.order_by('id').all()
        if len(contact):
            contact = contact[0]
        cart_ids = request.GET.getlist('cart')
        cart_ids_int = [int(_) for _ in cart_ids]
        carts = Cart.objects.filter(id__in=cart_ids_int)
        context = {
            'title': '提交订单',
            'carts': carts,
            'user': user,
            'contact': contact,
            'cart_ids': ','.join(cart_ids)
        }
        return render(request, 'order/place_order.html', context)
