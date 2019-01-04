from threading import Thread
from multiprocessing import Queue
import requests
from lxml import etree
from fake_useragent import UserAgent
import time
from urllib.parse import urlencode
import json
ua = UserAgent()


class XiaoMiSpider:
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?'
        self.mainurl = 'http://app.mi.com/'
        self.headers={'User-Agent':"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"}
        # URL队列
        self.urlQueue = Queue()
        # 解析队列
        self.parseQueue = Queue()
    # URL入队列
    def getUrl(self):
        for page in range(5):
            params = urlencode({'page':str(page),'categoryId':'2','pageSize':'30'})
            url = self.url + params
            # 把拼接的url地址放到url队列中
            print(url)
            self.urlQueue.put(url)
    # 采集线程函数,get出url发请求,把html给解析队列
    def getHtml(self):
        while True:
            # 先判断队列会否为空
            if not self.urlQueue.empty():
                url = self.urlQueue.get()
                # requests三步走
                res = requests.get(url,headers=self.headers)
                res.encoding = 'utf-8'
                html = res.text
                # 把html放到解析队列
                self.parseQueue.put(html)
            else:
                break
    # 解析线程函数, get出html源码, 提取并处理数据
    def getData(self):
        while True:
            if not self.parseQueue.empty():
            
                html = self.parseQueue.get()
                hList = json.loads(html)['data']
                for h in hList:
#                     应用名称
                    print(type(h))
#                    name = h['dsiplayName']
##                     应用链接
#                    link = 'http://app.mi.com/details?id='+h['packageName']
#                    d = {
#                            "分类":"学习教育",
#                            "应用名称":name,
#                            "应用链接":link,
#                            }
#                    with open('xiaoxiaomi.json','a',encoding='utf-8') as f:
#                        f.write(str(d) + '\n')
            else:
                break
            
                    
    def main(self):
        # url先入队列
        self.getUrl()
        # 存放所有采集线程对象列表
        t1List = []
        # 存放所有解析线程对象列表
        t2List = []
        # 采集线程
        for i in range(20):
            t = Thread(target = self.getHtml)
            t1List.append(t)
            t.start()
        # 统一回收采集线程
        for i in t1List:
            i.join()
        # 创建解析线程并干活
        for i in  range(20):
            f = Thread(target = self.getData)
            t2List.append(f)
            f.start()
        # 统一回收解析线程
        for i in t2List:
            i.join()
        

if __name__ == '__main__':
    start = time.time()
    spider = XiaoMiSpider()
    spider.main()
    end = time.time()
    print("执行时间:%.2f" % (end - start))