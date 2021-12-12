import pymysql

try:
    db = pymysql.connect(user='root', password='LHL618lhl', host='localhost', db='girls', port=3306, charset='utf8')
except Exception as e:
    print(f"连接失败，异常信息：{e}")
else:
    # 创建游标
    cur = db.cursor()
    sql = "insert into admin values(null,'小红','9999'),(null,'小懒','7777');"
    n = cur.execute(sql)
    print(n)
    db.commit()
    sql1 = "update admin set username='小黄' where id=14;"
    # 听过游标方法execute执行sql语句
    n = cur.execute(sql1)
    print(n)
    # 通过数据库对象的方法commit()提交事务才能生效
    db.commit()
    sql2 = "select * from admin;"
    n = cur.execute(sql2)
    print(cur.fetchone())
    print(cur.fetchone())
    print(cur.fetchmany(2))
    print(cur.fetchall())

    # sql3 = "delete from admin where id = 14;"
    # try:
    #     cur.execute(sql3)
    #     db.commit()
    # except Exception as e:
    #     db.rollback()
    #
    # # sql4 = "truncate table admin;"
    # # try:
    # #     cur.execute(sql4)
    # #     db.commit()
    # # except Exception as e:
    # #     db.rollback()

    # 关闭游标
    cur.close()
    # 关闭数据库连接
    db.close()
