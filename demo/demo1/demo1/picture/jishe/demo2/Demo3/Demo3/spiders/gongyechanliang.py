# -*- coding: utf-8 -*-
import scrapy
import json
import time


class GongyechanliangSpider(scrapy.Spider):
    name = 'gongyechanliang'
    allowed_domains = ['data.stats.gov.cn/']
    area = [110000, 120000, 130000, 140000, 150000, 210000, 220000, 230000, 310000, 320000, 330000, 340000, 350000,
            360000, 370000, 410000, 420000, 430000, 440000, 450000, 460000, 500000, 510000, 520000, 530000, 540000,
            610000, 620000, 630000, 640000, 650000]

    start_urls = [
        'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22{}%22%7D%5D&dfwds={}&k1={}'.
            format(valuecode, '[{"wdcode":"zb","valuecode":"A0E0B"}]', int(round(time.time() * 1000))) for valuecode in
        area]
    custom_settings = {
        'ITEM_PIPELINES': {'Demo3.pipelines.GongYePipeline': 300},
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
            'A0E0B01': '原油产量(万吨)	',
            'A0E0B02': '天然气产量(亿立方米)',
            'A0E0B03': '原盐产量(万吨)',
            'A0E0B04': '成品糖产量(万吨)',
            'A0E0B05': '啤酒产量(万千升、万吨)',
            'A0E0B06': '卷烟产量(亿支、万箱)',
            'A0E0B07': '纱产量(万吨)',
            'A0E0B08': '布产量(亿米)',
            'A0E0B09': '机制纸及纸板产量(万吨)',
            'A0E0B0A': '焦炭产量(万吨)',
            'A0E0B0B': '硫酸(折100%)产量(万吨)',
            'A0E0B0C': '烧碱(折100%)产量(万吨)',
            'A0E0B0D': '纯碱(碳酸钠)产量(万吨)',
            'A0E0B0E': '乙烯产量(万吨)',
            'A0E0B0F': '农用氮、磷、钾化肥产量(万吨)',
            'A0E0B0G': '化学农药原药产量(万吨)',
            'A0E0B0H': '初级形态的塑料产量(万吨)',
            'A0E0B0I': '化学纤维产量(万吨)',
            'A0E0B0J': '水泥产量(万吨)',
            'A0E0B0K': '平板玻璃产量(万重量箱)',
            'A0E0B0L': '生铁产量(万吨)',
            'A0E0B0M': '粗钢产量(万吨)',
            'A0E0B0N': '钢材产量(万吨)',
            'A0E0B0O': '金属切削机床产量(万台)',
            'A0E0B0P': '大中型拖拉机产量(万台)',
            'A0E0B0Q': '汽车产量(万辆)',
            'A0E0B0R': '轿车产量(万辆)',
            'A0E0B0S': '家用电冰箱产量(万台)',
            'A0E0B0T': '房间空调器产量(万台)',
            'A0E0B0U': '家用洗衣机产量(万台)',
            'A0E0B0V': '移动通信手持机产量(万台)',
            'A0E0B0W': '微型电子计算机产量(万台)',
            'A0E0B0X': '集成电路产量(万块)',
            'A0E0B0Y': '彩色电视机产量(万台)',
            'A0E0B0Z': '发电量(亿千瓦小时)',
            'A0E0B10': '水电发电量(亿千瓦小时)'
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
        for key, values in dict1.items():
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
