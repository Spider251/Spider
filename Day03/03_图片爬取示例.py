import requests
url = 'http://image001.server110.com/20170501/b0fcf54de40de65085ef34f59d07d2c8.jpg'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"}

res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
html = res.content
print(html)
with open("蛇皮.jpg",'wb') as f:
    f.write(html)