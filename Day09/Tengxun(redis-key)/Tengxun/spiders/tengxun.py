# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

from Tengxun.items import TengxunItem
from Tengxun.settings import *
from Tengxun.pipelines import *


class TengxunSpider(RedisSpider):
    name = "tengxun"
    allowed_domains = ["hr.tencent.com"]
    # 定义redis_key
    redis_key = 'tengxunspider:start_urls'
    url = "https://hr.tencent.com/position.php?start="
    def parse(self, response):
        # 把284页URL地址都给调度器入队列
        for i in range(0, 2831, 10):
            fullurl = "https://hr.tencent.com/position.php?start=" + str(i)
            # scrapy.Requests()
            # 将URL地址丢给调度器,同时告诉调度器,这个URL用parseHtml来解析
            yield scrapy.Request(fullurl, callback=self.parseHtml)

    def parseHtml(self, response):
        # 创建item对象
        item = TengxunItem()
        # 每个职位节点对象列表
        baseList = response.xpath('//tr[@class="even"] |//tr[@class="odd"]')
        for base in baseList:
            item['zhName'] = base.xpath('./td[1]/a/text()').extract()[0]
            item['zhType'] = base.xpath('./td[2]/text()').extract()
            if item['zhType']:
                item['zhType'] = item['zhType'][0]
            else:
                item['zhType'] = "无"
            item['zhNum'] = base.xpath('./td[3]/text()').extract()[0]
            item['zhAddress'] = base.xpath('./td[4]/text()').extract()[0]
            item['zhTime'] = base.xpath('./td[5]/text()').extract()[0]
            item['zhLink'] = base.xpath('./td[1]/a/@href').extract()[0]
            # 拼接完整职位链接
            url = "https://hr.tencent.com/" + item['zhLink']
            yield scrapy.Request(url,callback=self.parseJob,meta={'item':item})
    # 参数为子页面的response
    def parseJob(self,response):
        # item为上一行函数最后传递过来的item
        item = response.meta['item']
        # 岗位职责提取(用join()拼接成了字符串)
        baseList = response.xpath('//ul[@class="squareli"]')
        item['zhZhize'] = "".join(baseList[0].xpath('.//li').extract())
        item['zhYaoqiu'] = "".join(baseList[1].xpath('.//li').extract())
        yield item



