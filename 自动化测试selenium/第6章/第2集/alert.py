# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#拿到diver
driver = webdriver.Firefox()

#跳转网页
driver.get("file://///Mac/Home/Desktop/alert.html")

print(driver.title)

#睡眠时间3秒
sleep(2)

driver.find_element_by_id("alert").click()
#切换到弹窗
win = driver.switch_to_alert()
sleep(2)
win.accept()


driver.find_element_by_id("confirm").click()
#切换到弹窗
confirm_ele = driver.switch_to_alert()
sleep(2)
#confirm_ele.accept()
confirm_ele.dismiss()
