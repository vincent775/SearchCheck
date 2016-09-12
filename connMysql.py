# coding: UTF-8
import MySQLdb
def MySqlIN(sqlName,IP,Port=23000):
    try:
        conn = MySQLdb.connect(host=IP, user="root", passwd="", db="testdb",port=Port,charset="utf8")
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM "+sqlName)
        while (True):
            row = cursor.fetchone()
            if row == None:
               break
            return "%d" % (row[0])
        cursor.close()
        conn.close()
    except:
        return 0
