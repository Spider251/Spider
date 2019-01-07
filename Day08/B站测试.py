import requests
from fake_useragent import UserAgent
ua = UserAgent()
res = requests.get('https://live.bilibili.com/',headers={'User-Agent':ua.random})
res.encoding='utf-8'
html = res.text
print(html)