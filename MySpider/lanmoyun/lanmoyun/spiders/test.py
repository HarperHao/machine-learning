# import re
#
# a = '(107)'
# re.sub(r'[(]', '', a)
# print(a)
# !/usr/bin/env python
# coding=utf-8
import os

# import urllib.request
# import os
#
#
#
#
# def reporthook(a, b, c):
#     """
#     显示下载进度
#     :param a: 已经下载的数据块
#     :param b: 数据块的大小
#     :param c: 远程文件大小
#     :return: None
#     """
#     print("\rdownloading: %5.1f%%" % (a * b * 100.0 / c), end="")
#
#
# url = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
#
# urllib.request.urlretrieve(url, r'K:\编程\Python-2.7.5.tar.bz2',reporthook)
cookies = {'domain': 'www.mosoteach.cn', 'httpOnly': False, 'name': 'SERVERID', 'path': '/', 'secure': False,
           'value': '824d7c0284d1ee99b299799688267714|1590910166|1590910155'}, {'domain': 'www.mosoteach.cn',
                                                                                'expiry': 1590911980.021816,
                                                                                'httpOnly': True, 'name': 'acw_tc',
                                                                                'path': '/', 'secure': False,
                                                                                'value': '2f624a3315909101549937916e1e68f3122c312e4f1ad727eed7d07e2447dc'}, {
              'domain': 'www.mosoteach.cn', 'expiry': 1590917390.994682, 'httpOnly': True, 'name': 'teachweb',
              'path': '/', 'secure': False, 'value': '4d8cc0f998bd7473b5eadcd94f7434404421ce25'}, {
              'domain': 'www.mosoteach.cn', 'expiry': 1906270180, 'httpOnly': False, 'name': '_uab_collina',
              'path': '/web', 'secure': False, 'value': '159091018044993505745171'}
print("a b c".split())


def save_cookie(cookies):
    a, b, c, d = cookies
    SERVERID = a.get('value')
    acw_tc = b.get('value')
    teachweb = c.get('value')
    _uab_collina = d.get('value')
    str_cookie = "_uab_collina={}; acw_tc={}; teachweb={}; SERVERID={}".format(
        _uab_collina, acw_tc, teachweb, SERVERID
    )
    with open("lanmo_cookie.txt", 'w') as f:
        f.write(str_cookie)


def load_cookie():
    with open('lanmo_cookie.txt', 'r') as f:
        cookie = f.read()
    return cookie


cookies = [{'domain': 'www.mosoteach.cn', 'httpOnly': False, 'name': 'SERVERID', 'path': '/', 'secure': False,
            'value': '824d7c0284d1ee99b299799688267714|1590910166|1590910155'},
           {'domain': 'www.mosoteach.cn', 'expiry': 1590911980.021816, 'httpOnly': True, 'name': 'acw_tc', 'path': '/',
            'secure': False, 'value': '2f624a3315909101549937916e1e68f3122c312e4f1ad727eed7d07e2447dc'},
           {'domain': 'www.mosoteach.cn', 'expiry': 1590917390.994682, 'httpOnly': True, 'name': 'teachweb',
            'path': '/', 'secure': False, 'value': '4d8cc0f998bd7473b5eadcd94f7434404421ce25'},
           {'domain': 'www.mosoteach.cn', 'expiry': 1906270180, 'httpOnly': False, 'name': '_uab_collina',
            'path': '/web', 'secure': False, 'value': '159091018044993505745171'}]
load_cookie()
