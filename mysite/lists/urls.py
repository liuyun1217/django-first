# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 11:09 下午
@Auth ： LiuYun ZhaoYing
@File ：urls.py
@IDE ：PyCharm

"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home_page,name='home'),
]
