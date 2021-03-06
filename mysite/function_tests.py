# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 8:10 下午
@Auth ： LiuYun ZhaoYing
@File ：function_tests.py
@IDE ：PyCharm

"""

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from django.http import HttpRequest,HttpResponse
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 正常访问首页
        self.browser.get('http://localhost:8000/lists')
        # 看到网页的标题和头部都是'To-Do'
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # 提示输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        # 在文本框输入'Buy peacock feathers'
        inputbox.send_keys('Buy peacock feathers')

        # 按回车页面更新
        # 待办事项中显示了"1. Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        import time
        # time.sleep(30)
        # table = self.browser.find_element_by_id('id_list_table')
        # # table.switch_to_window(table.window_handles[1])
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn("1. Buy peacock feathers",[row.text for row in rows] )
        # self.assertTrue(any(row.text=='1. Buy peacock feathers' for row in rows),
        #                 "New to-do item did not appear in table -- its text was:\n%s" %(table.text))

        # 页面又显示了一个文本框，可以输入其他待办事项
        # 输入"Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table("1. Buy peacock feathers")
        self.check_for_row_in_list_table("2. Use peacock feathers to make a fly")
        self.fail('Finish the test!')



if __name__ == '__main__':
    unittest.main(warnings='ignore')