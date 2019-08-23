# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
#拿到diver
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
#跳转网页
# driver.get("file://///Mac/Home/Desktop/ratio.html")
driver.get("file:///E:/Python/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95selenium/%E7%AC%AC6%E7%AB%A0/%E7%AC%AC1%E9%9B%86/ratio.html")
print(driver.title)
print("默认选中male,2秒后选项female")
sleep(2)
driver.find_element_by_id("female").click()