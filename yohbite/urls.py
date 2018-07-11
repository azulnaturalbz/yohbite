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
from yohbiteapp import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^restaurant/sign-in/$', auth_views.login,
        {'template_name': 'restaurant/sign_in.html'},
        name='restaurant-sign-in'),
    url(r'^restaurant/sign-up/$', views.restaurant_sign_up,
        name='restaurant-sign-up'),
    url(r'^restaurant/sign-out/$', auth_views.logout,
        {'next_page': '/'},
        name='restaurant-sign-out'),
    url(r'^restaurant/$', views.restaurant_home, name='restaurant-home'),

    # sign in and sign up and sign out
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-token(sign in/sign up
    # /revoke-toke(sign out)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
