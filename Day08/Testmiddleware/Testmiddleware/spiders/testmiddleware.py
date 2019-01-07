# -*- coding: utf-8 -*-
import scrapy


class TestmiddlewareSpider(scrapy.Spider):
    name = 'testmiddleware'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print("我是parse函数的输出")
