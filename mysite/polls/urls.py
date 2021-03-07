# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/3 9:52 PM
@Auth ： LiuYun ZhaoYing
@File ：urls.py
@IDE ：PyCharm Community Edition

"""
from django.urls import path

from . import views
app_name = 'polls'



urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('test/', views.TestView.as_view(), name='test'),
    # path('test/', views.testurl, name='test'),
]