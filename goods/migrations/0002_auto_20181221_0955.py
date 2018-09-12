# Generated by Django 2.1.4 on 2018-12-21 09:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodscategory',
            options={'verbose_name_plural': 'Goods categories'},
        ),
        migrations.AlterField(
            model_name='goodsitem',
            name='brief',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='goodsitem',
            name='detail',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='goodsitem',
            name='in_stock',
            field=models.IntegerField(default=1),
        ),
    ]