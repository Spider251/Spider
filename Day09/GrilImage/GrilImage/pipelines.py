# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# scrapy定义了图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy


# class要继承图片管道类
class GrilimagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 获取图片的requests请求的方法

        yield scrapy.Request(url=item['image_url'])
