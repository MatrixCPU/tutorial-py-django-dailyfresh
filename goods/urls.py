from django.urls import path, re_path
from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.index, name='index'),
    path('lists/<int:category_id>/', views.list, name='list'),
    path('<int:id>/', views.detail, name='detail'),
    path('search/', views.GoodsSearchView(), name='search'),
]
