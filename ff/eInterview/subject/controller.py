from utils.sqlConnection import mysqlConnect

def subjectList(request):
    try:
        conn = mysqlConnect()
        sql = 'select * from subject'
        cur = conn.cursor()
        cur.execute(sql)
        output = cur.fetchall()
        print(output)
        return {"data":output}
    except Exception as e:
        print(e)


def getQuestions(request):
    try:
        id = request.args.get('id',type = int)
        conn = mysqlConnect()
        sql = 'SELECT * FROM questions WHERE subject_id = %s'
        val=[id]
        cur = conn.cursor()
        cur.execute(sql,val)
        output = cur.fetchall()
        print(output)
        return {"data":output}
    except Exception as e:
        print(e)


def createSub(request):
    data=request.get_json()
    subject=data.get('subject')
    conn = mysqlConnect()
    sql = 'INSERT INTO `subject` (`subject`) VALUES (%s);'
    val = [subject]
    cur = conn.cursor()
    try:
        cur.execute(sql,val)
        conn.commit()
        conn.close()
        return ({"msg":"success"})
    except Exception as e:
        print(e)
        return ({"msg":"fail"})
    

def updateSub(request):
    data=request.get_json()
    subject=data.get('subject')
    id = request.args.get('id',type = int)
    print(id, type(subject))
    conn = mysqlConnect()
    sql = '''UPDATE `subject` SET subject=%s WHERE id=%s'''
    val = [subject,id]
    cur = conn.cursor()
    try:
        cur.execute(sql,val)
        conn.commit()
        conn.close()
        return ({"msg":"success"})
    except Exception as e:
        print(e)
        return ({"msg":"fail"})



def deleteSub(request):
    id = request.args.get('id',type = int)
    conn = mysqlConnect()
    sql = 'DELETE FROM subject WHERE id=%s;'
    val = [id]
    cur = conn.cursor()
    try:
        cur.execute(sql,val)
        conn.commit()
        conn.close()
        return ({"msg":"success"})
    except Exception as e:
        print(e)
        return ({"msg":"fail"})

    