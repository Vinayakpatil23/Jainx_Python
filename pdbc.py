# import database
import sqlite3
from fileinput import close

# import schema
conn=sqlite3.connect("pdbc.db")

# create a cursor object
cursor=conn.cursor()

# create table
cursor.execute("""
    create table if not exists students(
    id integer primary key,
    name text not null,
    age integer,
    grade text)
""")

# insert records
# cursor.execute("insert into students values(?,?,?,?)",(1,"Alice",14,"A"))
# cursor.execute("insert into students values(?,?,?,?)",(2,"Bob",15,"B"))
# cursor.execute("insert into students values(?,?,?,?)",(3,"Charlie",14,"A"))
# conn.commit()

# retrieve records
cursor.execute("select * from students")
for row in cursor.fetchall():
    print(row)

# update a record
cursor.execute("update students set grade=? where name=?",("A+","Bob"))
conn.commit()

# delete a record
cursor.execute("delete from students where id=?",(3,))
conn.commit()


# close the connection
cursor.close()
conn.close()