from utils.sqlConnection import mysqlConnect

def registerUser():
    try:
        conn = mysqlConnect()
        cur = conn.cursor()
        
        sql1 = 'CREATE TABLE user ( id int(11) NOT NULL AUTO_INCREMENT,name varchar(25) NOT NULL, email varchar(25) NOT NULL, password varchar(25), role varchar(25) ,PRIMARY KEY (id), UNIQUE KEY (email));;'
        cur.execute(sql1)
        conn.commit()

        sql = 'INSERT INTO `user` (`id`, `name`, `email`, `password`, `role`) VALUES (1, "sudo", "sudo", "sudo@123", "sudo");'
        cur.execute(sql)
        conn.commit()
        conn.close()
        print("Sudo User Register")
    except Exception as e:
        print(e)