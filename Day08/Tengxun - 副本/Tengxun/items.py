# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


import scrapy


class TengxunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    zhName = scrapy.Field()
    # 类别
    zhType = scrapy.Field()
    # 人数
    zhNum = scrapy.Field()
    # 地点
    zhAddress = scrapy.Field()
    # 链接
    zhLink = scrapy.Field()
    # 时间
    zhTime = scrapy.Field()
    # 岗位职责
    zhZhize = scrapy.Field()
    # 岗位
    zhYaoqiu = scrapy.Field()



