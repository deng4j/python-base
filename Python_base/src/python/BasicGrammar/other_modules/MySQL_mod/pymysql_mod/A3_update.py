import pymysql

db = pymysql.connect(host="localhost", user="root",
                     password="159735", db="teacherdb", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

sql = "UPDATE student SET sGender = {} WHERE sName = '张三'".format(2)

try:
    cur.execute(sql)
    # 提交
    db.commit()
except Exception as e:
    # 错误回滚
    db.rollback()
finally:
    cur.close()
    db.close()
