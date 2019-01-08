# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
import json
from GrilImage.items import GrilimageItem

class GirlSpider(scrapy.Spider):
    name = 'girl'
    allowed_domains = ['image.so.com']

    # 把start_urls去掉, 重写start_requests()方法
    # 重写也就是自己指定要爬取的起始的URL地址
    def start_requests(self):
        baseurl = 'http://image.so.com/zj?'
        for i in range(0, 91, 30):
            params = {
                'ch': 'beauty',
                'sn': str(i),
                'listtype': 'new',
                'temp': '1',
            }
            url = baseurl + urlencode(params)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        item = GrilimageItem()
        # response.text是json格式的字符串, 需要转为字典
        imgList = json.loads(response.text)['list']
        # imgList : [{图片1信息},{图片2信息},{图片3信息},{图片4信息}]
        for img in imgList:
            item['image_url'] = img['qhimg_url']
            yield item






