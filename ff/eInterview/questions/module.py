from utils.sqlConnection import mysqlConnect

# def createTable():
try:
    conn = mysqlConnect()
    sql = 'CREATE TABLE questions ( id int(11) NOT NULL AUTO_INCREMENT,question varchar(500) NOT NULL,subject_id int(50),link varchar(500),teacher_id int(11),PRIMARY KEY (id));'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("questions table created")
except Exception as e:
    print(e)