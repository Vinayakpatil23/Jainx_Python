import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user='root',
    password="Patil@123",
    database="pdbc"
)

cursor=conn.cursor()

cursor.execute("""
    create table if not exists students(
    id integer primary key,
    name text not null,
    age integer,
    grade text)
""")

# cursor.execute("insert into students values(%s,%s,%s,%s)",(1,"Alice",14,"A"))
# cursor.execute("insert into students values(%s,%s,%s,%s)",(2,"Bob",15,"B"))
# cursor.execute("insert into students values(%s,%s,%s,%s)",(3,"Charlie",14,"A"))
# conn.commit()

cursor.execute("select * from students")
for row in cursor.fetchall():
    print(row)

cursor.execute("update students set grade=%s where name=%s",("A+","Bob"))
conn.commit()

cursor.execute("delete from students where id=%s",(3,))
conn.commit()

cursor.close()
conn.close()

