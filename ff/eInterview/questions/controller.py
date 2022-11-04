from utils.sqlConnection import mysqlConnect
from flask_jwt_extended import (get_jwt_identity)
# from eInterview.questions.model import createTable
# createTable()
def createQuestions(request):
    data=request.get_json()
    question=data.get('question')
    subject=data.get('subject')
    link=data.get('link')
    conn = mysqlConnect()
    user = get_jwt_identity()
    techer_id = user['id']
    sql = 'INSERT INTO `questions` (`question`, `subject_id`, `link`, `teacher_id`) VALUES (%s,%s,%s,%s);'
    val = [question,subject,link,techer_id]
    cur = conn.cursor()
    try:
        cur.execute(sql,val)
        conn.commit()
        conn.close()
        return ({"msg":"question added"})
    except Exception as e:
        print(e)
        return ({"msg":"fail"})

def listQuestions(request):
    try:
        conn = mysqlConnect()
        sql = 'select * from questions'
        cur = conn.cursor()
        cur.execute(sql)
        output = cur.fetchall()
        print(output)
        return {"data":output}
    except Exception as e:
        print(e)
    return ({"msg":"this is question list"})


def listOneById(request):
    try:
        id = request.args.get('id',type = int)
        conn = mysqlConnect()
        sql = 'select * from questions as que LEFT JOIN subject as sb ON sb.id = que.subject_id WHERE que.teacher_id=%s'
        val = [id]
        cur = conn.cursor()
        cur.execute(sql,val)
        output = cur.fetchall()
        print(output)
        return {"data":output}
    except Exception as e:
        print(e)
    return ({"msg":"this is question list"})


def updateQuestions(request):
    data=request.get_json()
    question=data.get('question')
    subject=data.get('subject')
    link=data.get('link')
    id = request.args.get('id',type = int)
    user = get_jwt_identity()
    techer_id = user['id']
    print(id, type(subject))
    conn = mysqlConnect()
    sql = '''UPDATE questions SET question=%s, subject_id=%s,link=%s, teacher_id=%s WHERE id=%s;'''
    val = [question,subject,link,techer_id,id]
    cur = conn.cursor()
    try:
        cur.execute(sql,val)
        conn.commit()
        conn.close()
        return ({"msg":"success"})
    except Exception as e:
        print(e)
        return ({"msg":"fail"})



def deleteQuestions(request):
    id = request.args.get('id',type = int)
    conn = mysqlConnect()
    sql = 'DELETE FROM questions WHERE id=%s;'
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
