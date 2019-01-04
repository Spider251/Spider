import requests
from lxml import etree

res = requests.get('https://blog.csdn.net/XiaoYi_Eric/article/details/85559389')
html = res.text
parseHtml = etree.HTML(html)
title = parseHtml.xpath('//h1[@class="title-article"]/text()')[0]
time = parseHtml.xpath('//span[@class="time"]/text()')[-1]
number = parseHtml.xpath('//span[@class="read-count"]/text()')[0]
print(title,time,number)