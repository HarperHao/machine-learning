"""查询"""
import sqlite3

# 创建连接
con = sqlite3.connect(r'K:\SQLite3\first_DB.db')
# 创建游标对象
cur = con.cursor()
sql = 'select * from t_person'
try:
    cur.execute(sql)
    persons=cur.fetchall()
    print(persons)
except Exception as e :
    print(e)
    print('查询失败')
finally:
    cur.close()
    con.close()
