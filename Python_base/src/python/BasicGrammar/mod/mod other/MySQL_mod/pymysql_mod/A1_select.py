import pymysql

"""
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount(): 这是一个只读属性，并返回执行execute()方法后影响的行数。
"""

db = pymysql.connect(host="localhost", user="root",
                     password="159735", db="teacherdb", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

sql = "select * from student"

cur.execute(sql)
results = cur.fetchall()  # 获取查询的所有记录

# 遍历结果
for row in results:
    sID = row[0]
    sNo = row[1]
    sName = row[2]
    print("{} {} {}".format(sID, sNo, sName))

cur.close()
db.close()
