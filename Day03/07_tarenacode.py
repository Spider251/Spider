# 爬取达内代码,保存到本地
import requests
import re
#import pymysql
#import warnings

class NoteSpider:
    def __init__(self):
        self.url = "http://code.tarena.com.cn/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}
        # Web客户端验证参数(元组)
        self.auth = ("tarenacode","code_2013")
        # 创建库对象
#        self.db = pymysql.connect("127.0.0.1","root","123456","spiderdb",charset="utf8")
        # 创建游标对象
#        self.cursor = self.db.cursor()
    # 获取并解析页面
    def getPrasePage(self):
        res = requests.get(self.url,headers=self.headers,auth=self.auth)
        res.encoding = "utf-8"
        html = res.text
        print(html)
        p = re.compile('<a href="(.*?)">.*?</a>',re.S)
        rList = p.findall(html)
        self.writePage(rList)
        print(rList[1:]) 
    # 保存数据
    def writePage(self,rList):
#        warnings.filterwarnings('ignore')
#        ctab = "create table if not exists tarenaNote(name varchar(30))"
#        ins = 'insert into tarenaNote values(%s)'
#        self.cursor.execute(ctab)
#        for r in rList:
#            self.cursor.execute(ins,[r])
#            # 提交到数据库中
#            self.db.commit()
#        # 关闭数据库
#        self.cursor.close()
#        self.db.close()
        with open('tarena.txt','a',encoding='utf-8') as f:
            for i in rList:
                f.write(i+'\n')
            
            
    
if __name__ == '__main__':
    spider = NoteSpider()
    spider.getPrasePage()