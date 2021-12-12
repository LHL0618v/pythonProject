import pymysql

try:
    db = pymysql.connect(user='root', password='LHL618lhl', host='localhost', db='girls', port=3306, charset='utf8')
except Exception as e:
    print(f"连接失败，异常信息：{e}")
else:
    # 创建游标
    cur = db.cursor()
    # %s是sql语句的参数，并非格式化字符串里的%s
    sql2 = "select * from admin where id=%s;"
    # 通过过游标方法execute执行sql语句
    n = cur.execute(sql2, 4)
    print(cur.fetchone())
    # 通过数据库对象的方法commit()提交事务才能生效
    db.commit()

    sql1 = "insert into admin(id,username,password) values(%s,%s,%s);"
    cur.execute(sql1, [0, "小李", '2464'])
    db.commit()

    # 关闭游标
    cur.close()
    # 关闭数据库连接
    db.close()
