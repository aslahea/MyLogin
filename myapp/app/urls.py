from django.urls import path
 
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('signout/', views.signout, name='signout'),
    path('register/', views.register, name='register'),
]