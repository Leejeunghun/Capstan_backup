import pymysql
import sys
import subprocess #GPIO control

var1 = sys.argv[1]
print(var1)


# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='qwer123',
                       db='esebird', charset='utf8')
 
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
    	subprocess.call('gpio -g write 21 0', sheell=True)
        print("close")
conn.close()
