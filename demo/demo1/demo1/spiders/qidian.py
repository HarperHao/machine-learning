# -*- coding: utf-8 -*-
import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['http://www.qidian.com/all']

    def parse(self, response):
        names = response.xpath('//h4/a/text()').extract()
        authers = response.xpath('//p[@class="author"]/a[1]/text()').extract()
        dict1 = {}
        k = zip(names, authers)
        for name, auther in k:
            dict1[name] = auther
        return dict1
