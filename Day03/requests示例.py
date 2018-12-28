import requests
url = "http://ww.baidu.com/"
headers = {"User-Agent":""}
res = requests.get(url,headers=headers)


res.encoding = "utf-8"

# 获取res的内容
print(res.text)


#获取响应的编码格式
print(res.encoding)





# 获取res的内容(bytes)
print(type(res.content))

#获取HTTP响应码()
print(res.status_code)

# 获取返回实际数据的URL地址
print(res.url)