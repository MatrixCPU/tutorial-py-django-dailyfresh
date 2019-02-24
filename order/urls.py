#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [path('', views.order, name='index')]
