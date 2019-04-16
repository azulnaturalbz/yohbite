from django.contrib import admin
from yohbiteapp.models import Restaurant, Customer, Driver, Meal, \
    Order,OrderDetails,MealType,Country,\
    District,Local,LocalType,Location
# Register your models here.


admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(MealType)
admin.site.register(Country)
admin.site.register(District)
admin.site.register(Local)
admin.site.register(LocalType)
admin.site.register(Location)


