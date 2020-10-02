# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class PicturePipeline(object):
    def process_item(self, item, spider):
        return item


class ImagePipline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item["image_urls"]:
            yield scrapy.Request(image_url, meta={"img_name": item['image_name']})

    def file_path(self, request, response=None, info=None):
        filename = request.meta['img_name'].strip().replace('\r\n\t\t', '')
        return filename.replace('/12', '') + '.jpg'
