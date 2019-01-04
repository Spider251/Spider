# -*- coding: utf-8 -*-
import scrapy
from Daomu.items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    key = input("请输入要爬取的数量")
    for i in range(0,int(key)):
        start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-' + str(i)]

    def parse(self, response):
        item = DaomuItem()
        # 所有章节列表
        aList = response.xpath('//article/a/text()').extract()
        # aList : ['七星鲁王 第一章 血尸']
        i = 0
        for a in aList:
            info = a.split()
            item["bookTitle"] = info[0]
            item["bookNum"] = info[1]
            item["bookName"] = info[2]
            item["bookLink"] = response.xpath('//article/a/@href').extract()[i]
            i += 1
            yield item
