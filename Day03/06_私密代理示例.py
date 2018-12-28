import requests

url = "http://httpbin.org/get"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"}
proxies = {"http":"http://309435365:szayclhp@112.74.108.33:16818"}

res = requests.get(url,headers=headers,proxies=proxies)
res.encoding = 'utf-8'
html = res.text
print(html)   