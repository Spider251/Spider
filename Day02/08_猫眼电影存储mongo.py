from urllib.request import urlopen,Request
import re
import pymongo


class MaoyanSpider:
    def __init__(self):
        self.base_url = 'https://maoyan.com/board/4?offset='
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}
        #连接对象
        self.conn = pymongo.MongoClient('192.168.213.128',27017)
        #库对象
        self.db = self.conn["MaoDB"]
        #集合对象
        self.myset = self.db['film']
    # 获取页面
    def getpage(self,url):
        req = Request(url,headers=self.headers)
        res = urlopen(req)
        html = res.read().decode()
        self.parsePage(html)
    # 解析页面
    def parsePage(self,html):
        p = re.compile('<dd>.*?<a.*?title="(.*?)".*?</a>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i>.*?fraction">(.*?)</i>',re.S)
        rList = p.findall(html)
        print(rList)
        self.writeToCsv(rList)
    #保存数据
    def writeToCsv(self,rList):
        for r in rList:
            d = {
                "name":r[0].strip(),
                "who":r[1].strip(),
                "releasetime":r[2].strip(),
            }
            self.myset.insert(d)
        print("OK")
            
    def main(self):
        num = input("爬取几页的内容:")
        for i in range(int(num)):
            self.getpage(self.base_url+str(i*10))
            print("爬取第%d页成功"%(i+1))
        print("程序结束")

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.main()