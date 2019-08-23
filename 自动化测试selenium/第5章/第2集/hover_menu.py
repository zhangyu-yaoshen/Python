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

#定位到鼠标移动到上面的元素
menu_ele = driver.find_element_by_css_selector("#app > div > div.main > div.banner.w > div.l_course_list > ul > li:nth-child(1)")

#对定位到的元素执行鼠标移动到上面的操作
ActionChains(driver).move_to_element(menu_ele).perform()

#选中子菜单
sub_meun_ele = driver.find_element_by_css_selector("#app > div > div.main > div.banner.w > div.innerbox > div.base > div.sort > a:nth-child(2)")

sleep(2)
sub_meun_ele.click()
