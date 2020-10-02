# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    # allowed_domains = ['login.com']
    start_urls = ['https://jxgl.image-ai.cn/jxgl/captcha']

    def parse(self, response):
        with open('yzm.jpg', 'wb') as f:
            f.write(response.body)
        code = input("请输入验证码:")
        form_data = {
            'userName': '1807004129',
            'pwd': '99816674',
            'verCode': code,
            'remember': 'y'
        }
        login_url = 'https://jxgl.image-ai.cn/jxgl/loginOpt'
        yield scrapy.FormRequest(login_url, callback=self.log_parse, formdata=form_data)

    def log_parse(self, response):
        print(response.text)
