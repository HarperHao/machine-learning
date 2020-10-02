"""数据的删除"""
import sqlite3

# 创建连接
con = sqlite3.connect(r'K:\SQLite3\first_DB.db')
# 创建游标对象
cur = con.cursor()
sql = 'delete from  t_person where pno=?'
try:
    cur.execute(sql, (2,))
    con.commit()
    print("删除成功")
except Exception as e:
    print(e)
    print('删除失败')
finally:
    cur.close()
    con.close()
