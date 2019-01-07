# -*- coding: utf-8 -*-
import scrapy
from Daomu.items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    base_url = 'http://www.daomubiji.com/dao-mu-bi-ji-'
    offset = 1
    start_urls = [base_url + str(offset)]


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
        if self.offset < 46:
            self.offset += 1
            url = self.base_url + str(self.offset)
            yield scrapy.Request(url,callback=self.parse)

