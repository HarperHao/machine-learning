"""修改数据"""
import sqlite3

# 创建连接
con = sqlite3.connect(r'K:\SQLite3\first_DB.db')
# 创建游标对象
cur = con.cursor()
sql = 'update t_person set pname=? where pno=?'
try:
    cur.execute(sql, ('hao', 1))
    con.commit()
    print("修改成功")
except Exception as e:
    print(e)
    print('修改失败')
finally:
    cur.close()
    con.close()
