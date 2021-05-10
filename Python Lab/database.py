
# 9 Database connectivity

'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE cricketers")
print('Database created !')

o/p:
Database created !
'''

# 1 Write a Python program to create table of cricketers data includes field like First_name, Last_name, Date_of_Birth, Place_of_Birth and Country using MySQL Database.
'''
import mysql.connector

mydb= mysql.connector.connect(
  host="localhost", user ="root", password="", database="cricketers"
)

mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE cricketers_data (First_name VARCHAR(50), Last_name VARCHAR(50), Date_of_birth DATE, Place_of_birth VARCHAR(100), Country VARCHAR(100))")
print('Table created !')

o/p:
Table created !
'''


# 2 Write a Python program to insert 5 cricketers’ data into created table for First_name, Last_name, Date_of_Birth, Place_of_Birth and Country.
'''
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="", database="cricketers")

mycursor=mydb.cursor()

sql= "INSERT INTO cricketers_data (First_name, Last_name, Date_of_birth, Place_of_birth, Country) VALUES (%s, %s, %s, %s, %s)"
value =[
  ('MahendraSingh','Dhoni','1981-07-07','Ranchi','India'),
  ('Sam','Curran','1998-06-03','Northampton','UK'),
  ('Ravindra','Jadeja','1988-12-06','Jamnagar','India'),
  ('KL', 'Rahul','1992-04-18','Bengaluru','India'),
  ('Faf','du Plessis','1984-07-13','Pretoria','South Africa')
]
mycursor.executemany(sql,value)

mydb.commit()

print(mycursor.rowcount, "cricketers inserted !")

o/p:
5 cricketers inserted !
'''

# 3 Write a Python program to select First_name  and Country values from Cricketers data.
'''
import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", password="", database="cricketers")

mycursor=mydb.cursor()

mycursor.execute("SELECT First_name, Country FROM cricketers_data ")

result=mycursor.fetchall()
for x in result:
  print(x)

o/p:
('MahendraSingh', 'India')
('Sam', 'UK')
('Ravindra', 'India')
('KL', 'India')
('Faf', 'South Africa')
'''


# 4 Write a Python program to update field Country into table of cricketers.
'''
import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", password="", database="cricketers")

mycursor=mydb.cursor()

mycursor.execute("UPDATE cricketers_data SET Country ='United Kingdom' WHERE First_name='Sam'")

mydb.commit()
print(mycursor.rowcount, "record updated !")

o/p:
1 record updated !
'''


# 5 Write a Python program to delete any one row from table of cricketer’s data.
'''
import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", password="", database="cricketers")

mycursor=mydb.cursor()

mycursor.execute("DELETE FROM cricketers_data WHERE Last_name='Rahul'")
mydb.commit()
print(mycursor.rowcount, "record deleted !")

o/p:
1 record deleted !
'''




