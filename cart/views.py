from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from user import decorators
from .models import Cart


@decorators.login_required
def cart(request):
    user_id = request.session.get('user_id', '')
    carts = Cart.objects.filter(user_id=user_id)
    context = {'title': '购物车', 'carts': carts}
    return render(request, 'cart/cart.html', context)


@decorators.login_required
def add(request):
    user_id = request.session.get('user_id', '')
    goods_id = int(request.GET['goods'])
    count = int(request.GET['count'])

    carts = Cart.objects.filter(user_id=user_id, goods_id=goods_id)
    if len(carts):
        cart = carts[0]
        cart.count += count
    else:
        cart = Cart()
        cart.user_id = user_id
        cart.goods_id = goods_id
        cart.count = count
    cart.save()  # update cart record

    if request.is_ajax():
        # return number of categories in cart
        count = Cart.objects.filter(user_id=user_id).count()
        return JsonResponse({'cart_id': cart.id, 'count': count})
    else:
        # TODO:
        #   1. Use ajax request when adding goods into cart
        #   2. Safety check for next URL
        next = request.META.get('HTTP_REFERER', None) or reverse('cart:index')
        return redirect(next)


@decorators.login_required
def status(request):
    '''count: return number of categories in the cart'''
    try:
        user_id = request.session.get('user_id', '')
        count = Cart.objects.filter(user_id=user_id).count()
    except Exception as e:
        count = 0
    return JsonResponse({'count': count})


@decorators.login_required
def edit(request):
    cart_id = int(request.GET['cart'])
    count = int(request.GET['count'])
    old_count = 1  # default
    try:
        cart = Cart.objects.get(pk=int(cart_id))
        # update cart count
        cart.count, old_count = count, cart.count
        cart.save()
        data = {'ok': 0}  # 0 for success
    except Exception as e:
        data = {'ok': old_count}
    return JsonResponse(data)


@decorators.login_required
def delete(request):
    cart_id = int(request.GET['cart'])
    try:
        cart = Cart.objects.get(pk=int(cart_id))
        cart.delete()
        data = {'ok': 0}
    except Exception as e:
        data = {'ok': 1}
    return JsonResponse(data)
