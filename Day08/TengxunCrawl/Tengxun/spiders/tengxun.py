# -*- coding: utf-8 -*-
import scrapy
# 只负责提取链接
from scrapy.linkextractors import LinkExtractor
# Rule 负责将提取出来的链接做解析
from scrapy.spiders import CrawlSpider, Rule
from Tengxun.items import TengxunItem

class TengxunSpider(CrawlSpider):
    name = 'tengxun'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?start=0']

    rules = (
        # allow 提取链接
        # callback 将提取出来的链接通过parse_item进行处理
        # follow 是否跟进处理
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parseTencent', follow=True),
        # 可以制定不同的RuLe,用来递归根据allow正则提取链接
        # Rule(LinkExtractor(allow=r'asdfg'),callback='parse2',follow=True)
    )

    def parseTencent(self, response):
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

