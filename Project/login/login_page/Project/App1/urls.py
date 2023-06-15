from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('one_login',views.one_login,name='one_login'),
    # path('home',views.home,name='home'),
    path('bsp_login',views.bsp_login,name='bsp_login'),
    path('home2',views.home2,name='home2'),




]