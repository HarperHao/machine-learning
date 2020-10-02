# -*- coding: utf-8 -*-
import scrapy


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://www.maoyan.com/films?catId={}showType=3'.format(i)
                  for i in range(1, 5)]

    def parse(self, response):
        names = response.xpath('//div[@class="channel-detail movie-item-title"]/@title').extract()
        scores_ = response.xpath('//div[@class="channel-detail channel-detail-orange"]').xpath('string(.)').extract()
        for name, score in zip(names, scores_):
            if response.url.find('catId=3'):
                type = "爱情片"
            elif response.url.find("catId=1"):
                type = "剧情片"
            elif response.url.find("catId=2"):
                type = "喜剧片"
            elif response.url.find("catId=4"):
                type = "动画片"
            yield {'name': name, 'score': score, 'type': type}
