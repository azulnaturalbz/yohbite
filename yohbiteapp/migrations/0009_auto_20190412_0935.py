# Generated by Django 2.2 on 2019-04-12 15:35

from django.db import migrations, models
import django.db.models.deletion
import yohbiteapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('yohbiteapp', '0008_driver_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('description', models.TextField(default='No Description')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yohbiteapp.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=100)),
                ('description', models.TextField(default='No Description')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yohbiteapp.District')),
            ],
        ),
        migrations.CreateModel(
            name='LocalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MealType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(upload_to=yohbiteapp.models.meals_upload_path),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(upload_to=yohbiteapp.models.restuarant_upload_path),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yohbiteapp.Local')),
                ('localType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yohbiteapp.LocalType')),
            ],
        ),
    ]
