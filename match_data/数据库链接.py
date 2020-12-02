import pymysql
from question import content
from question2 import content2
from 匹配题目 import data_back, get_single_question

db = pymysql.connect(host='localhost', user='zzf', password='zzf613', charset='utf8', database='question_tmp')
cursor = db.cursor()


def insert_data(t):
    sql = "INSERT INTO question (numbers,content, pic, options, answer, option_number, reference ) \
              VALUES ('%s','%s', '%s', '%s', '%s', '%s', '%s')" % \
          (t[0], t[1], t[2], t[3], t[4], t[5], t[6])
    cursor.execute(sql)


def search_data():
    pass


for i in get_single_question(content2):
    try:
        t = data_back(i)
        insert_data(t)
    except:
        pass
db.commit()
db.close()
