# -*- coding:gbk -*-
import pymssql

def MsSqlIN(sqlName):
    try:
        #����һ�����ݿ����ӣ�host�Ƿ�������ip��ַ������Ǳ���������"."��user�Ƿ����û�����password�����룬database�����ݿ�������ADO�������ƺ���һЩ
        conn=pymssql.connect(host="172.16.1.200",user="dbwriter",password="dbwriter@123",database="instrument")
        #conn=pymssql.connect(host=".",user="sa",password="123456",database="text")
        #�����α�����൱��ADO�ļ�¼��
        cou=conn.cursor()
        #����һ����¼
        sql = "select count(*) from " +sqlName
        cou.execute(sql)
        while (True):
            row = cou.fetchone()
            if row == None:
                break
            return "%d" % (row[0])
        #ֻ��ִ����������������Ĳ���������Ч������쳣��������ʵ��pymssql���������
        conn.commit()
        #�ر����ݿ������
        conn.close()
    except:
        return 0
if __name__=="__main__":
    MsSqlIN("")
