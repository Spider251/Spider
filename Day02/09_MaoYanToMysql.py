from urllib.request import urlopen,Request
import re
import pymysql
import warnings


class MaoyanSpider:
    def __init__(self):
        self.base_url = 'https://maoyan.com/board/4?offset='
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}
        self.db = pymysql.connect("localhost","root","123456","spiderdb",charset="utf8")
        # 创建游标对象
        self.cursor = self.db.cursor()
        
        
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
        # 忽略下面语句的所有警告
        warnings.filterwarnings("ignore")
        ins = 'insert into film(name,star,releasetime) values(%s,%s,%s)'
        for r in rList:
            L = [r[0].strip(),r[1].strip(),r[2].strip()]
            # execute必须使用列表传参
            self.cursor.execute(ins,L)
            self.db.commit()
            
    def main(self):
        num = input("爬取几页的内容:")
        for i in range(int(num)):
            self.getpage(self.base_url+str(i*10))
            print("爬取第%d页成功"%(i+1))
        self.cursor.close()
        self.db.close()
        print("程序结束")

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.main()