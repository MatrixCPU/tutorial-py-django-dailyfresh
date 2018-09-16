from django.db import models


class Order(models.Model):
    id = models.AutoField(max_length=20, primary_key=True)
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    # address = models.ForeignKey('user.Contact', on_delete=models.PROTECT)
    # save address as strings
    address = models.CharField(max_length=200)


class OrderItem(models.Model):
    item = models.ForeignKey('goods.GoodsItem', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField(default=1)
