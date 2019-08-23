#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Name    : test.py
Author  : Python
Time    : 2019/8/6 0006 12:31
"""

from selenium import webdriver
import time
# display = Display(visible=0, size=(1920, 1080))
# display.start()
driver=webdriver.Chrome()
driver.get("http://www.sogou.com")

# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')

# driver = webdriver.Chrome360()
# driver.get('http://www.baidu.com')

# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# __browser_url = r'D:\常用工具\360\360浏览器\360se6\Application\360se.exe'  ##360浏览器的地址
# chrome_options = Options()
# chrome_options.binary_location = __browser_url
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.baidu.com')
# driver.find_element_by_id("kw").send_keys("seleniumhq" + Keys.RETURN)
# time.sleep(3)
# driver.quit()