# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaiduPipeline(object):
    def process_item(self, item, spider):
        return item


class BaiduMongoPipeline(object):
    def process_item(self, item, spider):
        return item

class BaiduMysqlPipeline(object):
    def process_item(self, item, spider):
        return item