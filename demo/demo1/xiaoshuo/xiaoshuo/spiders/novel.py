# -*- coding: utf-8 -*-
import scrapy


class NovelSpider(scrapy.Spider):
    name = 'novel'
    # allowed_domains = ['novel.com']
    start_urls = ['https://www.biquge.lu/book/542/307167.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//*[@id="content"]/text()').extract()).replace(u'\xa0', '')
        yield {
            'title': title,
            'content': content
        }
        temp_url = response.xpath('//div[@class="page_chapter"]/ul/li[3]/a/@href').extract_first()
        next_url = response.urljoin(temp_url)
        # if temp_url != '/book/542/':
        yield scrapy.Request(next_url, callback=self.parse)
