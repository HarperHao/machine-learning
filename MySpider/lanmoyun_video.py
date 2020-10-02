"""
蓝墨云刷经验值
"""
import requests

url = "https://www.mosoteach.cn/web/index.php?c=res&m=save_watch_to"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Cookie": "_uab_collina=159059101078997376612166; UM_distinctid=172569cb06c2f1-0345c204d56898-4313f6a-144000-172569cb06d1f2; _ga=GA1.2.136553411.1590718825; acw_tc=707c9fd015960709840461356e24b85744fc6a22dd53ac413bcefd30acbca7; CNZZDATA1253495893=262530691-1590588989-https%253A%252F%252Fwww.baidu.com%252F%7C1596068863; teachweb=f9b88a5d8742c737fb0c3a1a47b1bde2fd16ec77; login_token=168f9e727e1c8466d68720bb0a9f5c403c7b1d44029577af80cc540dc0ceed7c; SERVERID=5da4142ab453b5c560efefb22dcfbe6a|1596071133|1596070984"
}
params = {
    'clazz_course_id': '5EB7E394-DC2E-48C4-9F84-5ABDA98DCFE6',
    'res_id': 'EF2CE573-8136-C911-5F25-24E5E939951B',
    'watch_to': '4000',
    'duration': '4000',  # 66min
    'current_watch_to': '0'
}

response = requests.post(url, data=params, headers=headers)
print(response.status_code)
