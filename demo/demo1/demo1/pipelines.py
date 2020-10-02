# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from operator import itemgetter
from itertools import groupby


class Demo1Pipeline(object):
    def open_spider(self, spider):
        self.file1 = open('剧情电影.txt', 'w', encoding='utf-8')
        self.file2 = open('喜剧电影.txt', 'w', encoding='utf-8')
        self.file3 = open('爱情电影.txt', 'w', encoding='utf-8')
        self.file4 = open('动画电影.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print(item)
        # self.file.write(json.dumps(item, ensure_ascii=False) + '\n')
        return item

    def close_spider(self, spider):
        self.file1.close()
        self.file2.close()
        self.file3.close()
        self.file4.close()
