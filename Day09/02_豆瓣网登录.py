from selenium import webdriver
from lxml import etree
from pytesseract import *
import time
import requests
from PIL import Image
from fake_useragent import UserAgent
ua = UserAgent()


# 访问豆瓣网得到html
url = 'https://www.douban.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(0.5)
# 把验证码图片的链接提取出来,并发起请求保存到本地
parseHtml = etree.HTML(driver.page_source)
rLink = parseHtml.xpath('//img[@id="captcha_image"]/@src')[0]
res = requests.get(rLink,headers={'User-Agent':ua.random})
res.encoding = 'utf-8'
html = res.content
with open('验证码.png','wb') as f:
    f.write(html)

# 把图片转为字符串
try:
    img = Image.open('验证码.png')
    result = image_to_string(img)
    print(result)
except:
    print("验证失败")
# 用户名.验证码.图片.登录豆瓣

driver.find_element_by_name('form_email').send_keys('1419418693@qq.com')
driver.find_element_by_name('form_password').send_keys('tt2008gax')
driver.find_element_by_id('captcha_field').send_keys(result)
time.sleep(2)
driver.find_element_by_class_name('bn-submit').click()

