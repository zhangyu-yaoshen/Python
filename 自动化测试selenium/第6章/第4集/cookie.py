# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#拿到diver
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
#跳转网页
driver.get("https://xdclass.net")
print(driver.title)
#睡眠时间3秒
sleep(3)
driver.add_cookie({"name":"name","value":"jack"})
driver.add_cookie({"name":"token","value":"xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cDovL3RoaXJkd3gucWxvZ28uY24vbW1vcGVuL3ZpXzMyL1EwajRUd0dUZlRKb0M3aWN6Y3F2cDc4dTFmMEhySmljZHJzNUtYWDgxdWRKVTQzMzlYNVEyWUtKd2xXSlVpYXZPU2Vnd1Z6U3RZTUNSWGQ5Nm52eXB5UE13LzEzMiIsImlkIjo3MywibmFtZSI6IuS6jOW9k-WutuWwj0QiLCJpYXQiOjE1MzgwNjY1MDgsImV4cCI6MTUzODY3MTMwOH0.Clm7FGGylmb6Acs_nRDcLyYzb8yv64LS_hIk16Wwkkg"})

video_ele = driver.find_element_by_css_selector("div.hotcourses:nth-child(3) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)")
video_ele.click()
sleep(2)

buy_btn_ele = driver.find_element_by_css_selector(".learn_btn > a:nth-child(1)")

buy_btn_ele.click()
print("进入下单页面")