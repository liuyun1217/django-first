# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 8:10 下午
@Auth ： LiuYun ZhaoYing
@File ：function_tests.py
@IDE ：PyCharm

"""

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')
assert 'Django' in browser.title