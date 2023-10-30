from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com/")
# 1、获取元素的属性
# content = driver.find_element(by=By.ID,value="su")
# print(content.get_attribute("class"))#获取标签的属性
# print(content.tag_name)#获取标签的名字
# a = driver.find_element(by=By.LINK_TEXT,value="新闻")
# print(a.text)#获取的是元素文本 
# 2、交互
time.sleep(3)
#搜索周杰伦
driver.find_element(by=By.ID,value="kw").send_keys("周杰伦")
time.sleep(3)
#点击百度一下
driver.find_element(by=By.ID,value="su").click()
time.sleep(3)
#划到底部
#模拟JS滚动
js_bottom = "document.documentElement.scrollTop=100000"
driver.execute_script(js_bottom)
time.sleep(3)
#点击下一页
driver.find_element(by=By.XPATH,value="//a[@class='n']").click()
time.sleep(3)
#点击后退
driver.back()
time.sleep(3)
#点击前进
driver.forward()
time.sleep(3)
#关闭浏览器
driver.quit()