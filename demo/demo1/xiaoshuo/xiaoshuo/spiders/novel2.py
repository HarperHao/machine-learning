# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Novel2Spider(CrawlSpider):
    name = 'novel2'
    #allowed_domains = ['biquge.com']
    start_urls = ['https://www.biquge.lu/book/542/307169.com']
    #start_urls = ['https://www.biquge.lu/book/542/307167.html']
    rules = (
        #目前的理解，没有看懂源代码，这个链接会把这两个rule都执行，rules是元组，必须得加个逗号
        Rule(LinkExtractor(restrict_xpaths=r'//dd[13]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="page_chapter"]/ul/li[3]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//*[@id="content"]/text()').extract()).replace(u'\xa0', '')
        yield {
            'title': title,
            'content': content
        }

