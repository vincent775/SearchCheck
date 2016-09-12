# -*- coding:gbk -*-
import pymssql

def MsSqlIN(sqlName):
    try:
        #创建一个数据库连接，host是服务器的ip地址，如果是本机可以用"."，user是访问用户名，password是密码，database是数据库名，比ADO的连接似乎简单一些
        conn=pymssql.connect(host="172.16.1.200",user="dbwriter",password="dbwriter@123",database="instrument")
        #conn=pymssql.connect(host=".",user="sa",password="123456",database="text")
        #创建游标对象，相当于ADO的记录集
        cou=conn.cursor()
        #插入一条记录
        sql = "select count(*) from " +sqlName
        cou.execute(sql)
        while (True):
            row = cou.fetchone()
            if row == None:
                break
            return "%d" % (row[0])
        #只有执行了下面的命令，上面的操作才能生效，配合异常处理，可以实现pymssql的事务操作
        conn.commit()
        #关闭数据库的连接
        conn.close()
    except:
        return 0
if __name__=="__main__":
    MsSqlIN("")
