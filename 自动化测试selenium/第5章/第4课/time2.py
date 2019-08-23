# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#拿到diver
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
#driver.implicitly_wait(10)  # 隐性等待，最长等10秒

#跳转网页
driver.get("https://baidu.com")

try:
	#显性等待
	ele = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID,"kw")))
	ele.send_keys("小D课堂")
	driver.find_element_by_id("su").click()

	print("资源加载成功")
	print(driver.title)
except:
	print("资源加载失败,发送报警邮件或者短信")

finally:
	print("不管有没成功，都打印，用于资源清理")
	#退出浏览器
	# driver.quit()

