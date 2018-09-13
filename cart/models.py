from django.db import models


class Cart(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    goods = models.ForeignKey('goods.GoodsItem', on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
