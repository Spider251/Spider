import requests
#import pymongo
from bs4 import BeautifulSoup

class LianjiaSpider:
    def __init__(self):
        self.url = 'https://ty.lianjia.com/ershoufang/pg'
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'}
        # 连接对象
#        self.conn = pymongo.MongoClient('127.232.4.43',27017)
        # 库对象
#        self.db = self.conn['Lianjia']
        # 集合对象
#        self.myset = self.db['houseInfo']
    # 获取页面
    def getPage(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parsePage(html)
    # 解析并保存页面
    def parsePage(self,html):
        # 创建解析对象
        soup = BeautifulSoup(html,'lxml')
        # 解析对象的find_all()方法获取每个房源信息
        rList = soup.find_all('li',attrs={'class':'clear LOGCLICKDATA'})
#        print(rList)
        for r in rList:
            Info = r.find('div',attrs={'class':'info clear'}).get_text().split('/')
            # 小区名称
            name = Info[0]
            # 户型
            huxing = Info[1]
            # 面积
            area = Info[2]
            ##################################################################################
            positionInfo = r.find('div',attrs={'class':'positionInfo'}).get_text().split('/')
            print(positionInfo)
            # 楼层
            louceng = positionInfo[0]
            # 年份
#            year = positionInfo[1]
            # 地点
#            address = positionInfo[2]
            ##################################################################################
            # 总价
            totalPrice = r.find('div',attrs={"class":"totalPrice"}).text.split('/')
            print(name,huxing,area,louceng)
            print("**********************************")
            d = {
                    "名称":name,
                    "户型":huxing,
                    "面积":area,
                    "楼层":louceng,
                    "总价":totalPrice,
                    }
            with open('链家.json','a',encoding='utf-8') as f:
                f.write(str(d) + '\n')
#            self.myset.insert_one(d)
            
        
    # 主函数
    def main(self):
        n= int(input("请输入页数:"))
        for pg in range(1,n+1):
            # 拼接url
            url = self.url + str(pg) + "/"
            self.getPage(url)
            print("第%d页抓取成功"%pg)
    
if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.main()