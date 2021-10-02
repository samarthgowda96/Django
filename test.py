import psycopg2

connection= psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="Mobile21!"
)

cursor=connection.cursor()
cursor.execute("select *  from company ")

rows= cursor.fetchall()
print(rows)
connection.commit()
cursor.close()

connection.close()