# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from xiaomi.settings import *

class XiaomiPipeline(object):
    def process_item(self, item, spider):
        print("--------------")
        print(item['title'])
        print(item['price'])
        print("--------------")
        return item

class MongoPipeline(object):
    def __init__(self):
        # 数据库连接对象
        self.conn = pymongo.MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)
        # 库对象
        self.db = self.conn[MONGODB_DB]
        # 集合对象
        self.myset = self.db[MONGODB_SET]
    def process_item(self, item, spider):
        d = dict(item)
        self.myset.insert_one(d)
        return item

class MysqlPipeline(object):
    def __init__(self):
        # 数据库连接对象
        self.db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PWD, database=MYSQL_DB,
                                  charset='utf8')
        # 创建游标对象
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'insert into jobs values(%s,%s)'
        L = [item['title'], item['price']]
        self.cursor.execute(ins, L)
        # 提交到数据库执行
        self.db.commit()
        return item

    # process_item处理完成后会执行此方法
    def close_spider(self, spider):
        print("MySQL数据库断开连接")
        self.cursor.close()
        self.db.close()


