# -*- coding: utf-8 -*-
import scrapy
import json


class AjaxSpider(scrapy.Spider):
    name = 'ajax'
    allowed_domains = ['data.stats.gov.cn']
    start_urls = [
        'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=reg&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A020101%22%7D%5D&dfwds=%5B%5D&k1=1586234059672&h=1']
    custom_settings = {
        'ITEM_PIPELINES': {'demo2.pipelines.MongoPipeline': 300},
    }

    def parse(self, response):
        text = json.loads(response.text)
        datanodes = text.get('returndata').get('datanodes')
        dict1 = {}
        area = {'zb.A020101_reg.110000_sj': '北京市',
                'zb.A020101_reg.120000_sj': '天津市',
                'zb.A020101_reg.130000_sj': '河北省',
                'zb.A020101_reg.140000_sj': '山西省',
                'zb.A020101_reg.150000_sj': '内蒙古自治区',
                'zb.A020101_reg.210000_sj': '辽宁省',
                'zb.A020101_reg.220000_sj': '吉林省',
                'zb.A020101_reg.230000_sj': '黑龙江省',
                'zb.A020101_reg.310000_sj': '上海市',
                'zb.A020101_reg.320000_sj': '江苏省',
                'zb.A020101_reg.330000_sj': '浙江省',
                'zb.A020101_reg.340000_sj': '安徽省',
                'zb.A020101_reg.350000_sj': '福建省',
                'zb.A020101_reg.360000_sj': '江西省',
                'zb.A020101_reg.370000_sj': '山东省',
                'zb.A020101_reg.410000_sj': '河南省',
                'zb.A020101_reg.420000_sj': '湖北省',
                'zb.A020101_reg.430000_sj': '湖南省',
                'zb.A020101_reg.440000_sj': '广东省',
                'zb.A020101_reg.450000_sj': '广西壮族自治区',
                'zb.A020101_reg.460000_sj': '海南省',
                'zb.A020101_reg.500000_sj': '重庆市',
                'zb.A020101_reg.510000_sj': '四川省',
                'zb.A020101_reg.520000_sj': '贵州省',
                'zb.A020101_reg.530000_sj': '云南省',
                'zb.A020101_reg.540000_sj': '西藏自治区',
                'zb.A020101_reg.610000_sj': '陕西省',
                'zb.A020101_reg.620000_sj': '甘肃省',
                'zb.A020101_reg.630000_sj': '青海省',
                'zb.A020101_reg.640000_sj': '宁夏回族自治区',
                'zb.A020101_reg.650000_sj': '新疆维吾尔自治区'
                }
        for node in datanodes:

            code = node.get("code")[:-5]
            if code not in dict1.keys():
                dict1[code] = []
            data = node.get("data").get("data")
            dict1[code].append(data)
        for key, values in dict1.items():
            yield {
                '地区': area[key],
                '2018(亿元)': values[1],
                '2017(亿元)': values[2],
                '2016(亿元)': values[3],
                '2015(亿元)': values[4],
                '2014(亿元)': values[5],
                '2013(亿元)': values[6],
                '2012(亿元)': values[7],
                '2011(亿元)': values[8],
                '2010(亿元)': values[9]
            }
