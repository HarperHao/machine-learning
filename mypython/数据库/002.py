"""插入多条数据"""
"""
sqlite3数据库创建表
"""
import sqlite3

# 创建连接
con = sqlite3.connect(r'K:\SQLite3\first_DB.db')
# 创建游标对象
cur = con.cursor()
# 创建表
sql = """
    insert into t_person(pname,age) values (?,?)
"""
# 执行
try:
    cur.executemany(sql, [('a', 23), ('b', 18), ('c', 50)])
    con.commit()
    print('插入多条数据成功')
except Exception as e:
    print(e)
    print("插入多条数据失败")
    con.rollback()
finally:
    cur.close()
    con.close()
