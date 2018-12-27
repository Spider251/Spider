# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 03:31:16 2018

@author: 达内
"""

from urllib.request import urlopen,Request
# 创建请求对象
all_url = "http://www.baidu.com/"
header={
    'User-Agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'        
}
url = Request(all_url,headers=header)
#获取响应对象
response = urlopen(url)
#获取内容
html = response.read().decode()
print(html)

#获取响应码
print(response.getcode())

#获取实际数据的URL
print(response.geturl())