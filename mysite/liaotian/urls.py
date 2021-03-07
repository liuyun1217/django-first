# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/6 12:07 下午
@Auth ： LiuYun ZhaoYing
@File ：urls.py
@IDE ：PyCharm

"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('main',views.main,name='main'),
    ]
