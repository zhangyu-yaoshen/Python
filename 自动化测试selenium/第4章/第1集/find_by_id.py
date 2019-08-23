# -*- coding: utf-8 -*-
from selenium import webdriver
#拿到diver
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
#跳转网页
driver.get("http://www.baidu.com")

print(driver.title)

#选中输入框，输入  “小D课堂”
driver.find_element_by_id("kw").send_keys("小D课堂")
#选中按钮，触发点击事件
driver.find_element_by_id("su").click()
#
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')