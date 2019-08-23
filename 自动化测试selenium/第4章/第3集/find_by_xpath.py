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

driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/ul/li[4]/a/div/img").click()
# driver.find_element_by_xpath("//*[@id="app"]/div/div[3]/div/div[2]/a[3]/div/img").click()

print(driver.title)