# -*- coding: utf-8 -*-
from selenium import webdriver
#拿到diver
driver = webdriver.Firefox()

#跳转网页
driver.get("http://www.baidu.com")

print(driver.title)

#选中输入框，输入  “小D课堂”
driver.find_element_by_class_name("s_ipt").send_keys("jmeter 小D课堂")
#选中按钮，触发点击事件
driver.find_element_by_id("su").click()