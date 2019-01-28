# -*- coding: utf-8 -*-
import scrapy
from xiaomi.items import XiaomiItem


class XxSpider(scrapy.Spider):
    # 项目名
    name = 'xx'
    # 允许爬取的域
    allowed_domains = ['search.mi.com']
    # 起始的URL

    url = 'https://search.mi.com/search_笔记本-'
    start_urls = [url+str(246)]

    def parse(self, response):
        for i in range(246,250):
            url = self.url + str(i)
            yield scrapy.Request(url, callback=self.parseHTML)

    def parseHTML(self, response):
        item = XiaomiItem()
        # 标题
        item['title'] = response.xpath('//div[@class="goods-list clearfix"]/div/h2/a/text()').extract()[0]
        # 价格
        item['price'] = response.xpath('//div[@class="goods-list clearfix"]/div/p/text()').extract()[0]
        yield item
