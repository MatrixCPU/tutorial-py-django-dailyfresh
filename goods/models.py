from django.db import models
from tinymce.models import HTMLField


class GoodsCategory(models.Model):
    name = models.CharField(max_length=20)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Goods categories'


class GoodsItem(models.Model):
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    # upload folder is relative to MEDIA_ROOT
    pic = models.ImageField(upload_to='goods')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    unit = models.CharField(max_length=10, default='500g')
    click = models.IntegerField(default=0)
    brief = models.CharField(max_length=120,null=True)
    detail = HTMLField(null=True)
    in_stock = models.IntegerField(default=10)
    is_promoted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
