import mysql.connector
conn=mysql.connector.connect(host='localhost',user='rami',passwd='12345')
cur=conn.cursor()
cur.execute("show databases")
for i in cur:
    print(i)