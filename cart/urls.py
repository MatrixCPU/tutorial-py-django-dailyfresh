from django.urls import path, re_path
from . import views

app_name = 'cart'

urlpatterns = [
    # damn, no query parameter is used
    path('', views.cart, name='index'),
    path('add/', views.add, name='add'),
    path('status/', views.status, name='status'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
    # re_path(r'^add(\d+)_(\d+)/$', views.add, name='add'),
    # re_path(r'^edit(\d+)_(\d+)/$', views.edit, name='edit'),
    # re_path(r'^delete(\d+)_(\d+)/$', views.delete, name='delete'),
]
