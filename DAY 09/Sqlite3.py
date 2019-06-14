import sqlite3
from pandas import DataFrame

#creating database
conn = sqlite3.connect ('db_University.db')

#creating cursor
c = conn.cursor()

c.execute("DROP Table employees;")
#giving names of table coloumns
c.execute ("""CREATE TABLE employees(
          Stud_Name  TEXT,
          Stud_Age INTEGER,
          Stud_roll_no INTEGER,
          Stud_branch TEXT
          )""")

#giving enteries
c.execute("INSERT INTO employees VALUES ('Doremon',19,123,'ME')")
c.execute("INSERT INTO employees VALUES ('Nobita',20,124,'CSE')")
c.execute("INSERT INTO employees VALUES ('Shinchan',11,125,'CSE')")
c.execute("INSERT INTO employees VALUES ('Susuka',21,126,'CSE')")
c.execute("INSERT INTO employees VALUES ('Dekisuki',22,124,'IT')")
c.execute("INSERT INTO employees VALUES ('Pikachu',22,124,'IT')")

c.execute("SELECT * FROM employees")


df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Name","Age","Roll_No","Branch"]

# commits the current transaction 
conn.commit()

# closing the connection 
conn.close()




