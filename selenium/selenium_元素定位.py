from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.baidu.com/")
#元素定位
#1、根据id找对象【*】
# browser.find_element(by=By.ID,value='kw').send_keys("selenium")
# browser.find_element(by=By.ID,value='su').click()
# sleep(3)
#2、根据name找对象
# button = browser.find_element(by=By.NAME,value='wd')
# sleep(3)
# print(button)
#3、根据class_name找对象
# input = browser.find_element(by=By.CLASS_NAME,value='s_ipt')
# print(input)
#4、根据tag_name找对象
# input = browser.find_element(by=By.TAG_NAME,value='input')
# print(input)
#5、根据xpath找对象 **注意:find_elements() 返回多个(哪怕是单个)都会生成一个列表【*】
# input = browser.find_element(by=By.XPATH,value='//*[@id="kw"]') #【find_element()返回一个不会形成列表】
# print(input)
#6、根据css找对象 bs4语法 【*】
# input = browser.find_element(by=By.CSS_SELECTOR,value='#kw')
# print(input)