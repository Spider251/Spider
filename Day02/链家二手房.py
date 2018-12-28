from urllib.request import urlopen,Request
from urllib.parse import urlencode
import re
class NeihanSpider:
    def __init__(self):
        self.base_url = 'https://ty.lianjia.com/ershoufang/pg1/'
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}
    # 获取页面
    def getPage(self,url):
        req = Request(url,headers=self.headers)
        res = urlopen(req)
        html = res.read().decode('utf-8')
        print("获取页面成功")
        self.parsePage(html)
    # 解析页面
    # 1.详情 
    # 2. 小区 
    # 3. | 4室2厅 | 165平米 | 南 北 | 精装 
    # 4.低楼层(共28层)板塔结合  -  
    # 5.关注情况
    # 6.180
    # 7. 万
    # 8. 占地面积
    def parsePage(self,html):
        a = '<li>.*?alt="(.*?)">.*?no_resblock_a">(.*?)</a>(.*?)</div>.*?<span class="positionIcon"></span>(.*?).*?<span class="starIcon"></span>(.*?).*?<div>.*?<div class="totalPrice"><span>(.*?)</span>(.*?)</div>.*?<div class="unitPrice" data-hid="101103841625" data-rid="8707131332518078" data-price="10910"><span>(.*?)</span></div>'
        p = re.compile('<li class="clea.*?alt="(.*?)".*?no_resblock_a">(.*?)</a>.*?</span>.*?"(.*?)".*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?',re.S)
        rList = p.findall(html)
        # rList [('',''),('','')]
        print(rList)
        print("页面解析成功")
        self.writePage(rList)
    # 保存数据
    def writePage(self,rList):
        pass
            
    # 主函数
    def main(self):
        self.getPage(self.base_url)
            
            
            
                
        
    
if __name__ == '__main__':
    spider = NeihanSpider()
    spider.main()