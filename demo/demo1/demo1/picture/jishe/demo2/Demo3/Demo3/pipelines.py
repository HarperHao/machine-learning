# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class MyPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        area = item["area"]
        del item["area"]
        database = self.client.农业
        collection = database[area]
        collection.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class ChanLiangPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        area = item["area"]
        del item["area"]
        database = self.client.主要农作物播种面积
        collection = database[area]
        collection.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class ChanLiangPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        area = item["area"]
        del item["area"]
        database = self.client.主要农作物播种面积
        collection = database[area]
        collection.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class NongCunRenKouPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        area = item["area"]
        del item["area"]
        database = self.client.乡村户数和乡村人口
        collection = database[area]
        collection.insert(item)
        return item


class GongYePipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        area = item["area"]
        del item["area"]
        database = self.client.工业产品产量
        collection = database[area]
        collection.insert(item)
        return item


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class MyPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        area = item["area"]
        del item["area"]
        database = self.client.农业
        collection = database[area]
        collection.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class MianJiPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        area = item["area"]
        del item["area"]
        database = self.client.AREA
        collection = database[area]
        collection.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class ChanLiangPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        area = item["area"]
        del item["area"]
        database = self.client.主要农作物播种面积
        collection = database[area]
        collection.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class NongCunRenKouPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        area = item["area"]
        del item["area"]
        database = self.client.乡村户数和乡村人口
        collection = database[area]
        collection.insert(item)
        return item


class MuBanPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        area = item["area"]
        del item["area"]
        db = '高等学校普通本、专科学校和学生情况'
        database = self.client[db]
        collection = database[area]
        collection.insert(item)
        return item
