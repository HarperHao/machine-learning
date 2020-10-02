# -*- coding: utf-8 -*-
import scrapy
import json
import time


class LiangshiSpider(scrapy.Spider):
    name = 'liangshi'
    allowed_domains = ['data.stats.gov.cn/']
    area = [110000, 120000, 130000, 140000, 150000, 210000, 220000, 230000, 310000, 320000, 330000, 340000, 350000,
            360000, 370000, 410000, 420000, 430000, 440000, 450000, 460000, 500000, 510000, 520000, 530000, 540000,
            610000, 620000, 630000, 640000, 650000]
    start_urls = [
        'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22{}%22%7D%5D&dfwds={}&k1={}'.
            format(valuecode, '[{"wdcode":"zb","valuecode":"A0D0Q"}]', int(round(time.time() * 1000))) for valuecode in
        area]
    custom_settings = {
        'ITEM_PIPELINES': {'demo2.pipelines.LiangShiPipeline': 300},
    }

    def parse(self, response):

        text = json.loads(response.text, encoding='utf-8')
        datanodes = text.get('returndata').get('datanodes')
        dict1 = {}
        areas = {'110000': '北京市',
                 '120000': '天津市',
                 '130000': '河北省',
                 '140000': '山西省',
                 '150000': '内蒙古自治区',
                 '210000': '辽宁省',
                 '220000': '吉林省',
                 '230000': '黑龙江省',
                 '310000': '上海市',
                 '320000': '江苏省',
                 '330000': '浙江省',
                 '340000': '安徽省',
                 '350000': '福建省',
                 '360000': '江西省',
                 '370000': '山东省',
                 '410000': '河南省',
                 '420000': '湖北省',
                 '430000': '湖南省',
                 '440000': '广东省',
                 '450000': '广西壮族自治区',
                 '460000': '海南省',
                 '500000': '重庆市',
                 '510000': '四川省',
                 '520000': '贵州省',
                 '530000': '云南省',
                 '540000': '西藏自治区',
                 '610000': '陕西省',
                 '620000': '甘肃省',
                 '630000': '青海省',
                 '640000': '宁夏回族自治区',
                 '650000': '新疆维吾尔自治区'
                 }
        choice = {
            'A0D0Q01': '粮食产量(万吨)',
            'A0D0Q02': '夏收粮食产量(万吨)',
            'A0D0Q03': '秋粮产量(万吨)',
            'A0D0Q04': '谷物产量(万吨)',
            'A0D0Q05': '稻谷产量(万吨)',
            'A0D0Q06': '早稻产量(万吨)',
            'A0D0Q07': '中稻和一季晚稻产量(万吨)',
            'A0D0Q08': '双季晚稻产量(万吨)',
            'A0D0Q09': '小麦产量(万吨)',
            'A0D0Q0A': '冬小麦产量(万吨)',
            'A0D0Q0B': '春小麦产量(万吨)',
            'A0D0Q0C': '玉米产量(万吨)',
            'A0D0Q0D': '谷子产量(万吨)',
            'A0D0Q0E': '高粱产量(万吨)',
            'A0D0Q0F': '其他谷物产量(万吨)',
            'A0D0Q0G': '大麦产量(万吨)',
            'A0D0Q0H': '豆类产量(万吨)',
            'A0D0Q0I': '绿豆产量(万吨)',
            'A0D0Q0J': '红小豆产量(万吨)',
            'A0D0Q0K': '大豆产量(万吨)',
            'A0D0Q0L': '薯类产量(万吨)',
            'A0D0Q0M': '马铃薯产量(万吨)',
            'A0D0Q0N': '棉花产量(万吨)',
            'A0D0Q0O': '油料产量(万吨)',
            'A0D0Q0P': '花生产量(万吨)',
            'A0D0Q0Q': '油菜籽产量(万吨)',
            'A0D0Q0R': '芝麻产量(万吨)',
            'A0D0Q0S': '葵花籽产量(万吨)',
            'A0D0Q0T': '胡麻籽产量(万吨)',
            'A0D0Q0U': '糖料产量(万吨)',
            'A0D0Q0V': '麻类产量(万吨)',
            'A0D0Q0W': '黄红麻产量(万吨)',
            'A0D0Q0X': '亚麻产量(万吨)',
            'A0D0Q0Y': '大麻产量(万吨)',
            'A0D0Q0Z': '苎麻产量(万吨)',
            'A0D0Q10': '甘蔗产量(万吨)',
            'A0D0Q11': '甜菜产量(万吨)',
            'A0D0Q12': '烟叶产量(万吨)',
            'A0D0Q13': '烤烟产量(万吨)',
            'A0D0Q14': '蔬菜产量(万吨)'
        }
        code = datanodes[0].get("wds")[1].get("valuecode")
        area = areas.get(code)

        for node in datanodes:
            valuecode = node.get("wds")[0].get("valuecode")
            name = choice.get(valuecode)
            if name not in dict1.keys():
                dict1[name] = []
            data = node.get('data').get('data')
            dict1[name].append(data)
        for key, values in dict1:
            yield {
                "area": area,
                "指标": key,
                '2018年': values[1],
                '2017年': values[2],
                '2016年': values[3],
                '2015年': values[4],
                '2014年': values[5],
                '2013年': values[6],
                '2012年': values[7],
                '2011年': values[8],
                '2010年': values[9]

            }
