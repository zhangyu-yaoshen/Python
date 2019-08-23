# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
#拿到diver
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐性等待，最长等10秒
#跳转网页
driver.get("https://baidu.com")
#睡眠时间3秒
#sleep(10)
print(driver.title)