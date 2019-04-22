import os
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
def restuarant_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)

    return '/'.join(['restuarants', str(instance.id),'restuarant_logos', filename])


def meals_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)

    return '/'.join(['restuarants', str(instance.restaurant.id),'restuarant_meals', filename])


class Country(models.Model):
    country = models.CharField(max_length=20)

    def __str__(self):
        return "%s " % (self.country)


class District(models.Model):
    district = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField(default='No Description')

    def __str__(self):
        return "%s " % (self.district)


class Local(models.Model):
    local = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    description = models.TextField(default='No Description')

    def __str__(self):
        return "%s " % (self.local)


class LocalType(models.Model):
    local = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s " % (self.local)


class Location(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    localType = models.ForeignKey(LocalType, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s " % (self.local)


class MealType(models.Model):
    local = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s " % (self.local)



class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    district = models.ForeignKey(District, on_delete=models.CASCADE,default=3)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,default=11)
    logo = models.ImageField(upload_to=restuarant_upload_path, blank=False)
    is_active = models.BooleanField(default=True)
    restaurant_index = models.PositiveIntegerField(default=99)


    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Meal(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to=meals_upload_path, blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    COOKING = 1
    READY = 2
    ONTHEWAY = 3
    DELIVERED = 4

    STATUS_CHOICES = (
        (COOKING, "Cooking"),
        (READY, "Ready"),
        (ONTHEWAY, "On the way"),
        (DELIVERED, "Delivered"),

    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=500)
    total = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    create_at = models.DateTimeField(default=timezone.now)
    picked_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_total = models.IntegerField()

    def __str__(self):
        return str(self.id)
