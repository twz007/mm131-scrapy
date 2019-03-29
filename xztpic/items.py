# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XztpicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #title为文件夹名字
    title = scrapy.Field()
    url = scrapy.Field()
    #图片的连接
    src = scrapy.Field()
    #alt为图片名字
    alt = scrapy.Field()
    referer = scrapy.Field()
    pass
