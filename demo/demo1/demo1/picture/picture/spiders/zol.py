# -*- coding: utf-8 -*-
import scrapy


class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/bizhi/8111_100887_2.html']

    def parse(self, response):
        image_url = response.xpath('//*[@id="bigImg"]/@src').extract()
        image_name = response.xpath('string(//h3)').extract_first()
        yield {
            "image_urls": image_url,
            "image_name": image_name
        }
        next_url = response.xpath('//*[@id="pageNext"]/@href').extract_first()
        if next_url.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
