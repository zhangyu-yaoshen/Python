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


#捕捉找不到元素异常 
try:
	driver.find_element_by_id("xdclass").click()
except:
	driver.get_screenshot_as_file("./error_png.png")


