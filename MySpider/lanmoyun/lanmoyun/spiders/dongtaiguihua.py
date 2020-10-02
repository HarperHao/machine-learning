# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class DongtaiguihuaSpider(scrapy.Spider):
    name = 'dongtaiguihua'

    # allowed_domains = ['baidu.com']
    def __init__(self):
        super().__init__()
        self.chrome = webdriver.Chrome()

    def start_requests(self):
        login_url = 'https://www.mosoteach.cn/web/index.php?c=passport&m=index'
        self.chrome.get(login_url)
        sleep(3)
        yield scrapy.Request(login_url, callback=self.parse)

    # def close(self, spider):
    #     self.chrome.quit()

    # 封装一个函数，用来判断某一结点的子结点是否存在
    def isElementPresent(self, node, model):
        """
        用来判断元素标签是否存在，
        """
        try:
            element = node.find_element_by_xpath(model)
        # 原文是except NoSuchElementException, e:
        except NoSuchElementException as e:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True

    def parse(self, response):
        username = '19834045107'
        password = '**lh000921'
        input1 = self.chrome.find_element_by_xpath("//form[@class='account-from']/input[1]")
        input1.send_keys(username)
        input2 = self.chrome.find_element_by_xpath(r"//form[@class='account-from']/input[2]")
        input2.send_keys(password)
        button = self.chrome.find_element_by_xpath(r"//button[@id='login-button-1']")
        button.click()
        sleep(3)
        # 进入到了主页面，保存登录时的cookie
        cookies = self.chrome.get_cookies()
        self.save_cookie(cookies)
        # 选择算法这一课程
        button_suanfa = self.chrome.find_element_by_xpath(
            r"//*[@id='main']/main/section[2]/div[3]/ul/li[10]/div[2]/span[2]")
        button_suanfa.click()
        sleep(3)
        # 进入到了算法页面
        # page_url = self.chrome.find_elements_by_xpath(r"//div[@class='interaction-row']")
        for i in range(0, 5):
            # 爬取算法第一个实验
            page_url = self.chrome.find_elements_by_xpath(r"//div[@class='interaction-row']")
            page_url[i].click()
            sleep(3)
            # 进入到了具体实验的界面
            # page = self.chrome.page_source
            # 实验名称
            title = self.chrome.find_element_by_xpath("//div[@id='title-text']").text
            # 学生总人数
            count = self.chrome.find_element_by_xpath("//*[@id='menu-content']/a[2]/span[2]").text.replace('(',
                                                                                                           '').replace(
                ')', '')
            for i in range(int(count) - 1):  # 去掉周文辉
                # 爬取第一个人
                name = self.chrome.find_elements_by_xpath("//div[@class='member-message']/span")[i].text
                homework_item = self.chrome.find_element_by_xpath(
                    "//*[@id='cc-main']/div[4]/div[{}]/div[3]".format(i + 3))
                content_detail = ".//div[@class='content-detail color-33 over']"
                attachment_model = ".//div[@class='homework-attachment-row']"
                content = ''
                temp_urls = []
                file_names = []
                if self.isElementPresent(homework_item, model=content_detail):
                    content = homework_item.find_element_by_xpath(content_detail).text
                if self.isElementPresent(homework_item, model=attachment_model):  # 这里不能用elif
                    # attachment_model = './/div[@class="homework-attachment-row"]'
                    attachment = homework_item.find_elements_by_xpath(
                        ".//div[@class='homework-attachment-row']")
                    attachment_length = len(attachment)
                    temp_url = 'https://www.mosoteach.cn/web/index.php?c=interaction_homework&m=attachment_url&clazz_course_id=3563C634-1047-11EA-9C7F-98039B1848C6&type=DOWNLOAD&id={}'
                    for i in range(attachment_length):
                        data_id = attachment[i].get_attribute("data-id")
                        temp_urls.append(temp_url.format(data_id))
                        file_name = attachment[i].find_element_by_xpath(
                            ".//div[@class='attachment-name color-33']").get_attribute('title')
                        file_names.append(file_name)
                print(name)
                yield {
                    "test_name": title,
                    "person_name": name,
                    "content": content,
                    "urls": temp_urls,
                    "filenames": file_names
                }
            self.chrome.back()
            sleep(3)
            print("执行成功")

    def save_cookie(self, cookies):
        a, b, c, d = cookies
        SERVERID = a.get('value')
        acw_tc = b.get('value')
        teachweb = c.get('value')
        _uab_collina = d.get('value')
        UM_distinctid = 'UM_distinctid=172569cb06c2f1-0345c204d56898-4313f6a-144000-172569cb06d1f2;'
        _ga = '_ga=GA1.2.136553411.1590718825;'
        CNZZDATA1253495893 = ' CNZZDATA1253495893=262530691-1590588989-https%253A%252F%252Fwww.baidu.com%252F%7C1592960772;'
        str_cookie = "_uab_collina={};".format(
            _uab_collina) + UM_distinctid + _ga + CNZZDATA1253495893 + "acw_tc={};teachweb={};SERVERID={}".format(
            acw_tc, teachweb, SERVERID)

        with open("lanmo_cookie.txt", 'w') as f:
            f.write(str_cookie)
