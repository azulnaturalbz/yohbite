"""yohbite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from yohbiteapp import views, api
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^$', views.home, name='home'),
                  url(r'^restaurant/sign-in/$', auth_views.LoginView.as_view(template_name='restaurant/sign_in.html'),
                      name='restaurant-sign-in'),
                  url(r'^restaurant/sign-up/$', views.restaurant_sign_up,
                      name='restaurant-sign-up'),
                  url(r'^restaurant/sign-out/$', auth_views.LogoutView.as_view(),
                      name='restaurant-sign-out'),
                  url(r'^restaurant/$', views.restaurant_home, name='restaurant-home'),

                  url(r'^restaurant/account/$', views.restaurant_account, name='restaurant-account'),
                  url(r'^restaurant/meal/$', views.restaurant_meal, name='restaurant-meal'),
                  url(r'^restaurant/meal/add/$', views.restaurant_add_meal, name='restaurant-add-meal'),
                  url(r'^restaurant/meal/edit/(?P<meal_id>\d+)/$', views.restaurant_edit_meal,
                      name='restaurant-edit-meal'),
                  url(r'^restaurant/order/$', views.restaurant_order, name='restaurant-order'),
                  url(r'^restaurant/report/$', views.restaurant_report, name='restaurant-report'),

                  # sign in and sign up and sign out
                  url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
                  # /convert-token(sign in/sign up
                  # /revoke-toke(sign out)
                  url(r'^api/restaurant/order/notification/(?P<last_request_time>.+)/$',
                      api.restaurant_order_notification),

                  # api for customers
                  url(r'^api/customer/restaurants/$', api.customer_get_restaurants),
                  url(r'^api/customer/meals/(?P<restaurant_id>\d+)/$', api.customer_get_meals),
                  url(r'^api/customer/order/add/$', api.customer_add_order),
                  url(r'^api/customer/order/lastest/$', api.customer_get_lastest_order),
                  url(r'^api/customer/driver/location/$',api.customer_driver_location),

                  #APIs for Drivers
                  url(r'^api/driver/orders/ready/$',api.driver_get_ready_orders),
                  url(r'^api/driver/order/pick/$', api.driver_pick_order),
                  url(r'^api/driver/orders/lastest/$', api.driver_get_lastest_order),
                  url(r'^api/driver/order/complete/$', api.driver_complete_order),
                  url(r'^api/driver/revenue/$', api.driver_get_revenue),
                  url(r'^api/driver/location/update/', api.driver_update_location),

                  # AJAX Rendering
                  path('ajax/load-district/', views.load_district, name="ajax_load_district"),
                  path('ajax/load-district/<int:did>/', views.load_district, name="ajax_load_district"),
                  path('ajax/load-location/', views.load_locations, name="ajax_load_locations"),
                  path('ajax/load-location/<int:did>/<int:lid>/', views.load_locations, name="ajax_load_locations"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
