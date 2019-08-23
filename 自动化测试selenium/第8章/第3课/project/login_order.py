# -*- coding: UTF-8 -*-
import unittest
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class LoginOrderTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.base_url = "https://xdclass.net"
        self.driver.get(self.base_url)


    def tearDown(self):
        print("单个测试用例结束")
        pass
        #单个测试用例结束
    
    def test_login_order(self):
        u"登录测试用例"
        driver = self.driver
        #登录框
        login_ele = driver.find_element_by_css_selector("#login")
        ActionChains(driver).click(login_ele).perform()

        sleep(2)
        #查找输入框,输入账号，输入框要提前清理里面的数据
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("13113777338")
        #查找密码输入框，输入密码
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys("123456789")

        #拿到登录按钮
        login_btn_ele = driver.find_element_by_css_selector("button.login")
        #触发点击事件,登录
        login_btn_ele.click()
        #判断登陆是否成功，逻辑-》鼠标移到上面，判断弹窗字符
        #获取鼠标上移的元素
        user_info_ele = driver.find_element_by_css_selector(".user_head_portrait")
        sleep(1)
        #hover触发
        ActionChains(driver).move_to_element(user_info_ele).perform()
        sleep(1)
        #获取用户名称元素
        user_name_ele = driver.find_element_by_css_selector(".img_name > span:nth-child(2)")
        print("===测试结果==")
        print(user_name_ele.text)

        name = user_name_ele.text
        #self.assertEqual(name, u"二当家小D",msg="登录失败")

        video_ele = driver.find_element_by_css_selector("div.hotcourses:nth-child(3) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)")
        video_ele.click()
        sleep(2)

        buy_btn_ele = driver.find_element_by_css_selector(".learn_btn > a:nth-child(1)")

        buy_btn_ele.click()
        print("进入下单页面")
       


if __name__ == '__main__':
       unittest.main()

   
