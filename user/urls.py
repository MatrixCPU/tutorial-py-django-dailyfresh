from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_check/', views.register_check, name='register_check'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('info/', views.info, name='info'),
    path('order/', views.order, name='order'),
    path('address/', views.address, name='address'),
]
