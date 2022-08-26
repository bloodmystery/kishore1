"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from dj import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('home',views.index,name="home"),
    path('blind',views.blind,name="blind"),
    path('deaf',views.deaf,name="deaf"),
    path('paralyzed',views.paralyzed,name="paralyzed"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('slb',views.slb,name="slb"),
    path('flb',views.flb,name="flb"),
    path('slb1',views.slb1,name="slb1"),
    path('flb1',views.flb1,name="flb1"),
    path('sld',views.sld,name="sld"),
    path('fld',views.fld,name="fld"),
    path('sld1',views.sld1,name="sld1"),
    path('fld1',views.fld1,name="fld1"),
    path('slp',views.slp,name="slp"),
    path('flp',views.flp,name="flp"),
    path('slp1',views.slp1,name="slp1"),
    path('flp1',views.flp1,name="flp1"),
]
