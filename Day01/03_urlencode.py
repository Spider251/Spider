from urllib.request import Request,urlopen
from urllib.parse import urlencode
key = input("请输入要搜索的内容:")
# 定义百度url
baseurl = "http://www.baidu.com/s?"
# 模拟头访问
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'        
}
# 进行urlencode编码,参数为字典
key = urlencode({'wd':key})
# 拼接url
url = baseurl + key
# 创建请求对象
req = Request(url,headers=headers)
# 获取响应对象
response = urlopen(req)
# 获取内容
html = response.read().decode('utf-8')

# 保存到本地文件,encoding参数指定文件编码
with open("美女.html",'w',encoding='gb18030') as f:
    f.write(html)