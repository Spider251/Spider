from selenium import webdriver
from lxml import etree
from pytesseract import *
import time
import requests
from PIL import Image
from fake_useragent import UserAgent

ua = UserAgent()


# 访问豆瓣网得到html
num = 0
while True:
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
    with open('douban.png','wb') as f:
        f.write(html)
    time.sleep(2)
    # 把图片转为字符串

    # img = Image.open('douban.png')
    # result = image_to_string(img)

    # 用户名.验证码.图片.登录豆瓣
    from YDM import *
    cid, result = yundama.decode(filename, codetype, timeout)
    print(result)

    driver.find_element_by_name('form_email').send_keys('1419418693@qq.com')
    driver.find_element_by_name('form_password').send_keys('tt2008gax')
    driver.find_element_by_id('captcha_field').send_keys(result)
    time.sleep(2)
    driver.find_element_by_class_name('bn-submit').click()
    if num == 10:
        break

