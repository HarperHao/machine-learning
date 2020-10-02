import urllib.request

headers = ('User-Agent',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
           )
cookies = ('Cookie',
           '_uab_collina=159059101078997376612166; UM_distinctid=172569cb06c2f1-0345c204d56898-4313f6a-144000-172569cb06d1f2; CNZZDATA1253495893=262530691-1590588989-https%253A%252F%252Fwww.baidu.com%252F%7C1590715109; acw_tc=707c9fd115907187967255680e7af6d987754f089a4f0f6e932aa5c22b6f8e; _ga=GA1.2.136553411.1590718825; _gid=GA1.2.992466820.1590718825; _gat_web=1; SERVERID=fa9dfdff9e021f4fa153a3b543909010|1590718801|1590718796; teachweb=36d74aa8ba0b573e3373a3b42b651c7cf0353359')
opener = urllib.request.build_opener()
opener.addheaders = [headers,cookies]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(
    'https://www.mosoteach.cn/web/index.php?c=interaction_homework&m=attachment_url&clazz_course_id=3563C634-1047-11EA-9C7F-98039B1848C6&type=DOWNLOAD&id=206453679',
    r'1.py')
