import time as t
from selenium import webdriver

driver = webdriver.Chrome()
# 访问指定对象
driver.get("http://www.baidu.com")
# 基于ID定位"kw"元素，输入框，输入虚竹搜索条件
driver.find_element('id', 'kw').send_keys("虚竹")
# 基于ID定位"su"元素，点击1次百度一下
driver.find_element('id', 'su').click()
# 强制等待五秒
t.sleep(5)
driver.quit()

