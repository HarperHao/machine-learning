# -*- coding: utf-8 -*-
import scrapy


class NongyeSpider(scrapy.Spider):
    name = 'nongye'
    allowed_domains = ['data.stats.gov.cn/']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
