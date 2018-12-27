'https://tieba.baidu.com/f?kw=妹子&pn=50'
from urllib.parse import urlencode
from urllib.request import urlopen,Request
import random
import time

hList = [
        {'User-Agen':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'},
        {'User-Agen':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'},

]
# 随机生成列表中的头部信息
headers = random.choice(hList)

name = input("请输入要抓取的贴吧名称:")
start = int(input("请输入起始页:"))
end = int(input("请输入终止页:"))

base_url = 'http://tieba.baidu.com/f?'
kw = urlencode({'kw':name})
for page in range(start,end+1):
    # 拼接第page页完整的URL地址
    pn = (page - 1) * 50
    req = Request(base_url+kw+'&pn='+str(pn),headers=headers)
    res = urlopen(req)
    html = res.read().decode('utf-8')
    with open('妹子第%d页.html'% page,'w',encoding='utf-8') as f:
        f.write(html)
    print("第%d页爬取成功"%page)
    time.sleep(0.5)
