import pymysql


conn= pymysql.connect(
    host='119.3.179.82',
    user='re',
    password='motevision',
    charset='utf8',
    database='gp'
)



cur = conn.cursor()
sqli="select * from info"
result=cur.execute(sqli)
print(result)
info = cur.fetchall()
print(info)
cur.close()
conn.close()