# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os.path
import urllib.request


class LanmoPipeline(object):
    def load_cookie(self):
        with open('lanmo_cookie.txt', 'r') as f:
            cookie = f.read()
        return cookie

    def process_item(self, item, spider):

        # def reporthook(a, b, c):
        #     """
        #     显示下载进度
        #     :param a: 已经下载的数据块
        #     :param b: 数据块的大小
        #     :param c: 远程文件大小
        #     :return: None
        #     """
        #     print("\r{0}downloading:{1}%".format(item["person_name"], a * b * 100.0 / c), end="")

        # 先创建总文件夹
        foldername = r'.\{}'.format("算法")
        if not os.path.exists(foldername):
            os.makedirs(foldername)
        # 创建个人文件夹
        person_folder = r'.\算法\{0}\{1}'.format(item["test_name"], item["person_name"])
        if not os.path.exists(person_folder):
            os.makedirs(person_folder)
        if item['content'] != '':
            with open(r'.\算法\{0}\{1}\content.txt'.format(item["test_name"], item["person_name"]), 'w')as f:
                f.write(item['content'])
        if item["urls"] is not []:
            for i in range(len(item['urls'])):
                filepath = person_folder + '/' + item['filenames'][i]
                headers = ('User-Agent',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
                           )
                cookie = self.load_cookie()
                cookies = ('Cookie', cookie)
                opener = urllib.request.build_opener()
                opener.addheaders = [headers, cookies]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(item['urls'][i], filename=filepath)
