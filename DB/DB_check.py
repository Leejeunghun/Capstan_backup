import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='qwer123',db='esebird', charset='utf8',port=3306)
 
curs = conn.cursor()
 
sql = "select * from member"
curs.execute(sql)
 

rows = curs.fetchall()
print(rows[1][5]) 
conn.close()
