# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    bookTitle = scrapy.Field()
    bookNum = scrapy.Field()
    bookName = scrapy.Field()
    bookLink = scrapy.Field()
