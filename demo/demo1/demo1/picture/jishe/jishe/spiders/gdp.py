# -*- coding: utf-8 -*-
import scrapy


class GdpSpider(scrapy.Spider):
    name = 'gdp'
    # allowed_domains = ['gdp.com']
    start_urls = ['http://data.stats.gov.cn/easyquery.htm?cn=E0103']

    # 爬取2018-2015各个地区的gdp总值（亿元）
    def parse(self, response):
        area = response.xpath("//div/div[3]//tr/td[1]/text()").extract()  # 不同地区
        year_2018 = response.xpath("//div/div[3]//tr/td[2]/text()").extract()  # 2018gdp
        year_2017 = response.xpath("//div/div[3]//tr/td[3]/text()").extract()
        year_2016 = response.xpath("//div/div[3]//tr/td[4]/text()").extract()
        year_2015 = response.xpath("//div/div[3]//tr/td[5]/text()").extract()
        for area_, year_2018_, year_2017_, year_2016_, year_2015_ in zip(area, year_2018, year_2017, year_2016,
                                                                         year_2015):
            yield {
                "area": area_,
                "2018GDP": year_2018_,
                "2017GDP": year_2017_,
                "2016GDP": year_2016_,
                "2015GDP": year_2015_
            }
