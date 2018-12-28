import requests

base_url = "https://www.baidu.com/s?"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"}

title = input("搜索内容:")
pn = input("输入页数:")
pn = (int(pn)-1)*10
params = {
        'wd':title,
        'pn':pn
}
# 无需拼接url地址, 无需URL编码
res = requests.get(base_url,params=params,headers=headers)
res.encoding = "utf-8"
html = res.text
print(html)