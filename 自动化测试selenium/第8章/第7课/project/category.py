# -*- coding: UTF-8 -*-
import unittest
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class CategoryTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.base_url = "https://xdclass.net"
        self.driver.get(self.base_url)


    def tearDown(self):
        print("测试结束")
        #单个测试用例结束
        self.driver.quit()

    def test_menu(self):
        u"弹出菜单测试用例"
        driver = self.driver
        #跳转网页
        sleep(1)

        #定位到鼠标移动到上面的元素
        menu_ele = driver.find_element_by_css_selector("#banner_left_ul > a:nth-child(1) > li:nth-child(1) > span:nth-child(1)")

        #对定位到的元素执行鼠标移动到上面的操作
        ActionChains(driver).move_to_element(menu_ele).perform()
        sleep(2)
        #选中子菜单
        sub_meun_ele = driver.find_element_by_css_selector("#des > li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")

        sub_meun_ele.click()
        sleep(2)


if __name__ == '__main__':
    unittest.main()

   
