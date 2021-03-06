# Generated by Django 2.1.4 on 2018-12-26 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20180908_1640'),
        ('goods', '0002_auto_20181221_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.Contact')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('count', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsItem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
        ),
    ]
