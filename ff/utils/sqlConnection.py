import pymysql

def mysqlConnect():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root', 
            password = "",
            db='technors',
            )
        return conn
    except Exception as e:
        print(e)
    