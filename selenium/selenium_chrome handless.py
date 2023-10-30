from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#path是你chrome浏览器的路径
path = "C:\Program Files\Google\Chrome\Application\chrome.exe"#唯一可改的
chrome_options.binary_location = path

browser = webdriver.Chrome(options=chrome_options)

browser.get('https://www.baidu.com')
browser.save_screenshot('./selenium/baidu.png')