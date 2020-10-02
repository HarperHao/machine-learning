# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class TongjijuPipeline(object):
    def process_item(self, item, spider):
        def open_spider(self, spider):
            self.client = pymongo.MongoClient()

        def process_item(self, item, spider):
            area = item["area"]
            del item["area"]
            self.client.economy.area.insert(item)
            return item

        def close_spider(self, spider):
            self.client.close()
