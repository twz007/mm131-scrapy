# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from xztpic.items import XztpicItem

'''
广度优先
'''
class BreadthMm131Spider(CrawlSpider):
    name = 'mm131_breadth'
    allowed_domains = ['mm131.com']
    start_urls = ['http://www.mm131.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.mm131.com/.+/\d+_*\d*.html'), callback='img_item', follow=True),
    )

    def img_item(self, response):
        item = XztpicItem()
        selector = Selector(response)
        pattern = re.compile(r'\(\d+\)')
        item['title'] = selector.xpath("//h5/text()").extract_first()
        item['title'] = re.sub(pattern=pattern, repl='', string=item['title'])
        item['src'] = selector.xpath("//div[@class='content-pic']/a/img/@src").extract()
        item['alt'] = selector.xpath("//div[@class='content-pic']/a/img/@alt").extract()
        item['url'] = response.url
        item['referer'] = response.url
        #print(item)
        yield item


    # def parse(self, response):
    #     item = XztpicItem()
    #     selector = Selector(response)
    #     item['title'] = selector.xpath("//h5/text()").extract_first()
    #     item['src'] = selector.xpath("//div[@class='content-pic']/a/img/@src").extract_first()
    #     item['alt'] = selector.xpath("//div[@class='content-pic']/a/img/@alt").extract_first()
    #     item['url'] = response.url
    #     item['referer'] = response.url
    #     yield item

'''
深度优先
'''
class DepthMm131Spider(CrawlSpider):
    name = 'mm131_depth'
    allowed_domains = ['mm131.com']
    start_urls = ['http://www.mm131.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.mm131.com/.+/\d+.html'), callback='img_item', follow=True),
    )

    def img_item(self, response):
        item = XztpicItem()
        selector = Selector(response)
        pattern = re.compile(r'\d+')
        item['title'] = selector.xpath("//h5/text()").extract_first()
        item['src'] = selector.xpath("//div[@class='content-pic']/a/img/@src").extract()
        root_src = str(item['src'][0][:item['src'][0].rindex('/')]) + '/'
        item['alt'] = selector.xpath("//div[@class='content-pic']/a/img/@alt").extract()
        root_alt = str(item['alt'][0])
        item['url'] = response.url
        item['referer'] = response.url

        num = selector.xpath("//span[@class='page-ch'][1]/text()").extract_first()
        num = int(pattern.findall(num)[0])
        #根据规律拼接当前图集下的所有图片
        item['src'] += [root_src + str(i+1) + '.jpg' for i in range(num) if i > 0]
        item['alt'] += [re.sub(pattern=pattern, repl=str(i+1), string=root_alt) for i in range(num) if i > 0]
        #print(item)
        yield item


    # def parse(self, response):
    #     item = XztpicItem()
    #     selector = Selector(response)
    #     item['title'] = selector.xpath("//h5/text()").extract_first()
    #     item['src'] = selector.xpath("//div[@class='content-pic']/a/img/@src").extract_first()
    #     item['alt'] = selector.xpath("//div[@class='content-pic']/a/img/@alt").extract_first()
    #     item['url'] = response.url
    #     item['referer'] = response.url
    #     yield item