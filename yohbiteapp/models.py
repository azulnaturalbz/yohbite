import os
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.core.exceptions import ValidationError
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.db.models import PositiveIntegerField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from simple_history.models import HistoricalRecords
from django_extensions.db import fields as extension_fields


# Create your models here.
def restuarant_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)

    return '/'.join(['shops', str(instance.id),'shop_logos', filename])


def meals_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)

    return '/'.join(['shops', str(instance.restaurant.id),'shop_items', filename])


class Country(models.Model):
    # Fields
    country_name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='country_name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    history = HistoricalRecords()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.country_name)

    def get_absolute_url(self):
        return reverse('yohbiteapp_country_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('yohbiteapp_country_update', args=(self.slug,))


class District(models.Model):
    # Fields
    district_name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='district_name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    history = HistoricalRecords()

    # Relationship Fields
    country = models.ForeignKey(
        'yohbiteapp.Country',
        on_delete=models.CASCADE, related_name="districts",
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.district_name)

    def get_absolute_url(self):
        return reverse('yohbiteapp_district_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('yohbiteapp_district_update', args=(self.slug,))


class LocalType(models.Model):
    # Fields
    local_type_name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='local_type_name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    history = HistoricalRecords()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.local_type_name)

    def get_absolute_url(self):
        return reverse('yohbiteapp_localtype_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('yohbiteapp_localtype_update', args=(self.slug,))

class Local(models.Model):
    # Fields
    local_name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='local_name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    history = HistoricalRecords()

    # Relationship Fields
    local_district = models.ForeignKey(
        'yohbiteapp.District',
        on_delete=models.CASCADE, related_name="locals",
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.local_name)

    def get_absolute_url(self):
        return reverse('yohbiteapp_local_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('yohbiteapp_local_update', args=(self.slug,))


class Location(models.Model):
    # Fields
    location_description = models.TextField(max_length=255, blank=True)
    slug = extension_fields.AutoSlugField(populate_from='local', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    history = HistoricalRecords()

    # Relationship Fields
    local = models.ForeignKey(
        'yohbiteapp.Local',
        on_delete=models.CASCADE, related_name="locations",
    )
    local_type = models.ForeignKey(
        'yohbiteapp.LocalType',
        on_delete=models.CASCADE, related_name="locations",
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.local)

    def get_absolute_url(self):
        return reverse('yohbiteapp_location_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('yohbiteapp_location_update', args=(self.slug,))


class MealType(models.Model):
    meal_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s " % (self.meal_type)



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
    #TODO ADD QUANTITY FOR STOCK AND MINUS QUANTITY WITH ORDER
    #TODO ADD CATEGORY FOR ITEMS
    #TODO CHANGE INTEGER FIELD FOR MEAL TO POSITIVE DECIMAL
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to=meals_upload_path, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # is_sale = models.BooleanField(default=false)
    # sale_discount = models.PositiveIntegerField(default=0)
    # is_available = models.BooleanField(default=false)
    # stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    #TODO ADD PHONE NUMBER
    REQUESTED = 1
    CONFIRMED = 2
    READY = 3
    COMPLETED = 4
    CANCELLED = 5

    STATUS_CHOICES = (
        (REQUESTED, "Requested"),
        (CONFIRMED, "Confirmed"),
        (READY, "Ready"),
        (COMPLETED, "Completed"),
        (CANCELLED, "Cancelled")

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
