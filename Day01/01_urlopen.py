# 向百度发起请求并得到response响应对象
from urllib.request import urlopen,Request

all_url = "http://www.baidu.com/"
response = urlopen(all_url)
print(response.read().decode('utf-8'))

# decode() : bytes - > string 
# encode() : string - > bytes