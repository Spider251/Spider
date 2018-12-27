from urllib.request import urlopen,Request
import re
import csv


class MaoyanSpider:
    def __init__(self):
        self.base_url = 'https://maoyan.com/board/4?offset='
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}
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
            r = [r[0].strip(),r[1].strip(),r[2].strip(),r[3],r[4]]
            with open('猫眼.csv','a',newline="",encoding="gb18030") as f:
                # 创建写入对象
                writer = csv.writer(f)
                # 调用writerow()方法
                writer.writerow(r)
    def main(self):
        num = input("爬取几页的内容:")
        for i in range(int(num)):
            self.getpage(self.base_url+str(i*10))
            print("爬取第%d页成功"%(i+1))
        print("程序结束")

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.main()