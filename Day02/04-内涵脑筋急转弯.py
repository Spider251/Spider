from urllib.request import urlopen,Request
from urllib.parse import urlencode
import re

class NeihanSpider:
    def __init__(self):
        self.base_url = 'https://www.neihan8.com/njjzw/'
        self.headers = {"User-Agent":""}
        self.page = 2
    # 获取页面
    def getPage(self,url):
        req = Request(url,headers=self.headers)
        res = urlopen(req)
        html = res.read().decode('utf-8')
        print("获取页面成功")
        self.parsePage(html)
    # 解析页面
    def parsePage(self,html):
        p = re.compile('<div class="text-.*?title="(.*?)">.*?class="desc">(.*?)</div>',re.S)
        rList = p.findall(html)
        # rList [('',''),('','')]
        print("页面解析成功")
        self.writePage(rList)
    # 保存数据
    def writePage(self,rList):
        for rTuple in rList:
            with open("内涵.txt","a") as f:
                f.write(rTuple[0].strip()+"\n")
                f.write(rTuple[1].strip()+"\n\n")
        print("页面保存成功")
    # 主函数
    def main(self):
        self.getPage(self.base_url)
        while True:
            c = input("成功,是否继续(Y/N):")
            if c.strip().lower() == 'y':
                url = self.base_url+'index_%d.html'%self.page
                self.getPage(url)
                self.page+=1
            else:
                print("程序结束")
                break
                
        
    
if __name__ == '__main__':
    spider = NeihanSpider()
    spider.main()