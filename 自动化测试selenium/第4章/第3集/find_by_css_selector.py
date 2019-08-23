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
# driver.find_element_by_css_selector(".type_content > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)").click()
driver.find_element_by_css_selector("#app > div > div.hot > div > div.content > a:nth-child(1) > div > img").click()
print(driver.title)