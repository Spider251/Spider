from urllib.request import urlopen,Request
from urllib.parse import urlencode
import re
import csv
class NeihanSpider:
    def __init__(self):
        self.base_url = 'https://maoyan.com/board/4?offset='
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}
    # 获取页面
    def getPage(self,url):
        req = Request(url,headers=self.headers)
        res = urlopen(req)
        html = res.read().decode('utf-8')
        print("获取页面成功")
        self.parsePage(html)
    # 解析页面
    def parsePage(self,html):
        p = re.compile('<dd>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i>.*?fraction">(.*?)</i>',re.S)
        rList = p.findall(html)
        # rList [('',''),('','')]
        print("页面解析成功")
        self.writePage(rList)
    # 保存数据
    def writePage(self,rList):
        for rTuple in rList:
            with open("猫眼.txt","a") as f:
#                writer = csv.writer(f)
#                writer.writerow([rTuple[0].strip(),rTuple[1].strip(),rTuple[2],+rTuple[3]])
                f.write(rTuple[0].strip()+"\n")
                f.write(rTuple[1].strip()+"\n\n")
                f.write("最高:"+rTuple[2]+"最低:"+rTuple[3]+"\n\n")
    # 主函数
    def main(self):
        for i in range(2):
            self.getPage(self.base_url+str(i*10))
            
            
            
                
        
    
if __name__ == '__main__':
    spider = NeihanSpider()
    spider.main()