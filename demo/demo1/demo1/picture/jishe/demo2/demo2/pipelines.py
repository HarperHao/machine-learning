# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class MongoPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.economy.GDP.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class PopulationPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.economy.年末常住人口.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class JuMinPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.economy.居民消费价格指数.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class ShouRuPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.economy.居民人均可支配收入.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class JiuYePipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.economy.城镇单位就业人员.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class ChuShengLvPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.economy.人口出生率.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class PingJunGongZiPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.economy.城镇就业人员平均工资.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class RenKouMiDuPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.economy.城市人口密度.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class ShuiZiYuanPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.economy.人均水资源量.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class XiangCunRenKouPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.economy.乡村人口.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class LiangShiPipeline(object):

    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        area = item["area"]
        del item["area"]
        self.client.economy.area.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class CarPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.运输.私人汽车拥有量.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class TieLuPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.运输.铁路营业里程.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class KuaiDiPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.运输.快递量.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class InternetPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.运输.互联网上网人数.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class LvYouPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.旅游.接待国际游客数.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class MuBanPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.卫生.医疗卫生机构数.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()
