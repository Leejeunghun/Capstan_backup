import pymysql
import sys
import subprocess #GPIO control

from datetime import datetime
now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")


# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='qwer123',db='esebird', charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 
# SQL문 실행a
sql = "select * from member"
curs.execute(sql)
 
# 데이타 Fetch
rows = curs.fetchall()
for row in rows:
    print(row[5])
    if row[5]=='{}'.format(sys.argv[1]):
        subprocess.call('gpio -g write 21 1', shell=True)
        conn_item = pymysql.connect(host='localhost',user='root',password='qwer123',db='esebird',charset='utf8')
        curs_item= conn_item.cursor()
        sql_item = "insert into item(User,Door_status,time) values(%s,%s,%s)"
        curs_item.execute(sql_item,(row[1],'Open',date_time))
        conn_item.commit()
        conn_item.close()
        print("OK")
conn.close()
