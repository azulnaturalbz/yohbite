# Generated by Django 2.0.7 on 2018-07-15 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yohbiteapp', '0005_orderdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='quantity',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='sub_total',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]
