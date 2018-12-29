import requests
from lxml import etree

class QiuShiSpider:
    def __init__(self):
        self.url = "http://www.qiushibaike.com/text/"
        self.headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}
        # 连接对象
#        self.conn = pymongo.MongoClient("172.232.4.35",27017)
        # 库对象
#        self.db = self.conn['Qiushidb']
        # 集合对象
#        self.myset = self.db["zhuanye"]
    
    def getPage(self):
        
        res = requests.get(self.url,headers=self.headers)
        
        res.encoding = 'utf-8'
        html = res.text
        self.parsePage(html)
    def parsePage(self,html):
        parseHtml = etree.HTML(html)
        # 基准Xpath,每个段子对象
        baseList = parseHtml.xpath('//div[contains(@id,"qiushi_tag_")]')
        # for 循环遍历每个段子对象,1个1个提取
        for base in baseList:
            # base : <element at ...>节点对象
            # 用户昵称
            username = base.xpath('./div/a/h2')[0].text
            if username:
                username = username[0]
            else:
                username = "匿名用户"
            # 段子内容
            content = base.xpath('./a/div[@class="content"]/span')[0].text
            content = "".join(content).strip()
            # 好笑数量
            laughNum = base.xpath('.//i[@class="number"]')[0].text
            # 评论数量
            pinglunNum = base.xpath('.//i[@class="number"]')[1].text
            # 定义字典存mongo
#            d = {
#                 "username":username,
#                 "content":content,
#                 "laughNum":laughNum,
#                 "pinglunNum":pinglunNum,
#                    }
            self.myset.insert_one(d)
        with open('糗事百科.txt','a') as f:
            f.write(username+"\n")
            f.write(content+"\n")
            f.write(laughNum+"   ")
            f.write(pinglunNum+"\n")
        
    def main(self):
        print("正在爬取中......")
        self.getPage()
        print("爬取结束,存入Qiushidb库")

if __name__ == '__main__':
    spider = QiuShiSpider()
    spider.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        