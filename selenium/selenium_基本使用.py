#导入selenium
from selenium import webdriver
#创建浏览器操作对象
browser = webdriver.Chrome()
#访问网站
# browser.get('https://www.baidu.com')
browser.get('https://www.jd.com')
#page_source()获取网页源码
content = browser.page_source
print(content)
