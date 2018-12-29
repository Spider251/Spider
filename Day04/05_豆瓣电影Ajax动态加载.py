import requests
import json
#import pymysql

class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}
#        self.db = pymysql.connect("","tiger","123456","spiderdb",charset='utf8')
    # 获取页面
    def getPage(self,params):
        res = requests.get(self.url,params=params,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        # html为[{1个电影信息},{},{}]
        self.parsePage(html)
    # 解析页面
    def parsePage(self,html):
#        ins = "insert into film values(%s,%s)"
        rList = json.loads(html)
        for rDict in rList:
            name = rDict["title"]
            score = rDict["score"]
            print(name,score)
            L = [name.strip(),float(score.strip())]
#            self.cursor.execute(ins,L)
            with open('豆瓣电影.txt','a') as f:
                f.write(name+"   ")
                f.write(score+"\n\n")
    
    #主函数
    def main(self):
        number = input("请输入数量:")
        params = {
            'type':'11',
            'interval_id':'100:90',
            'action':"",	
            'start':"0",
            'limit':number
            }
        self.getPage(params)

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.main()
    
