# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaomiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 笔记本信息
    title = scrapy.Field()
    # 价格
    price = scrapy.Field()