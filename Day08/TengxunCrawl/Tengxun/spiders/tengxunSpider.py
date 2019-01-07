# -*- coding: utf-8 -*-
import scrapy
from Tengxun.items import TengxunItem
from Tengxun.settings import *
from Tengxun.pipelines import *


class TengxunSpider(scrapy.Spider):
    name = "tengxun2"
    allowed_domains = ["hr.tencent.com"]
    # 基准URL, 方便后续做URL拼接
    url = 'http://hr.tencent.com/position.php?start='
    start_urls = [url + str(0)]

    def parse(self, response):
        # 把284页URL地址都给调度器入队列
        for i in range(0, 2831, 10):
            url = self.url + str(i)
            # scrapy.Requests()
            # 将URL地址丢给调度器,同时告诉调度器,这个URL用parseHtml来解析
            yield scrapy.Request(url, callback=self.parseHtml)

    def parseHtml(self, response):
        # 创建item对象
        item = TengxunItem()
        # 每个职位节点对象列表
        baseList = response.xpath('//tr[@class="even"] |//tr[@class="odd"]')
        for base in baseList:
            item['zhName'] = base.xpath('./td[1]/a/text()').extract()[0]
            item['zhType'] = base.xpath('./td[2]/text()').extract()[0]
            item['zhNum'] = base.xpath('./td[3]/text()').extract()[0]
            item['zhAddress'] = base.xpath('./td[4]/text()').extract()[0]
            item['zhTime'] = base.xpath('./td[5]/text()').extract()[0]
            item['zhLink'] = base.xpath('./td[1]/a/@href').extract()[0]
            yield item



