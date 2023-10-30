#Phantomjs公司黄了
#只是换了一个驱动器，其他一致
#加一个save_screenshot()方法，截图
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("https://www.baidu.com/")
driver.save_screenshot('./selenium/baidu1.png')