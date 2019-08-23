# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#拿到diver
driver = webdriver.Firefox()

#跳转网页
driver.get("https://xdclass.net")

print(driver.title)
#睡眠时间3秒
sleep(3)


#登录框
login_ele = driver.find_element_by_css_selector("#login")
#触发点击事件
ActionChains(driver).click(login_ele).perform()

sleep(1)
#查找输入框,输入账号，输入框要提前清理里面的数据
driver.find_element_by_id("phone").clear()
driver.find_element_by_id("phone").send_keys("13113777338")

#查找密码输入框，输入密码
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("12345678")


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

if name == u"二当家小D":
	print("login ok")
else:
	print("login fail")