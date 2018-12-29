import requests


url = "http://tieba.baidu.com/p/5964890031"
headers = {'User-Agent','User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}

res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
html = res.text

with open('1.html','a',encoding='utf-8') as f:
    f.write(html)