# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Daomu.settings import *
import pymysql
import pymongo

class DaomuPipeline(object):
    def process_item(self, item, spider):
        return item

# class MongoPipeline(object):
#     def __init__(self):
#         self.conn = pymongo.MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)
#         self.db = self.conn[MONGODB_DB]
#         self.myset = self.db[MONGODB_SET]
#     def process_item(self,item,spider):
#         # 把item转换为字典格式
#         d = dict(item)
#         self.myset.insert_one(d)
#         return item

class MysqlPipeline(object):
    def __init__(self):
        # 数据库连接对象
        self.db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PWD, database=MYSQL_DB,
                                  charset='utf8')
        # 创建游标对象
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'insert into books values(%s,%s,%s,%s)'
        L = [item['bookTitle'], item['bookNum'], item['bookName'], item['bookLink']]
        self.cursor.execute(ins, L)
        # 提交到数据库执行
        self.db.commit()
        return item

    # process_item处理完成后会执行此方法
    def close_spider(self, spider):
        print("MySQL数据库断开连接")
        self.cursor.close()
        self.db.close()