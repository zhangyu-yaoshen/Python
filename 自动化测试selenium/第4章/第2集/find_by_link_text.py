# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
#拿到diver
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
#跳转网页
driver.get("https://xdclass.net")
print(driver.title)
#睡眠时间3秒
sleep(3)
driver.find_element_by_link_text("视频学习").click()