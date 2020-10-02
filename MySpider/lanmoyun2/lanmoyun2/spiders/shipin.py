# -*- coding: utf-8 -*-
import scrapy


class ShipinSpider(scrapy.Spider):
    name = 'shipin'
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
