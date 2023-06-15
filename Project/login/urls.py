from django.urls import include,path
from .import views

urlpatterns = [
    path('sighnup',views.sighnup,name="sighnup"),
    path('log',views.log,name='log'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),

]