from bs4 import BeautifulSoup   
import requests

import sqlite3
#creating database
conn = sqlite3.connect ('icc.db')

#creating cursor
c = conn.cursor()

#c.execute("DROP Table employees;")
#giving names of table coloumns
c.execute ("""CREATE TABLE icc(
          Country  TEXT,
          Weight TEXT,
          Points TEXT,
          Rating TEXT
          )""")

#c.execute("DROP TABLE icc;")

icc = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(icc).text
soup = BeautifulSoup(source,"lxml")
#print (soup.prettify())
right_table=soup.find('table', class_='table')
#print (right_table.prettify())

for row in right_table.findAll('tr'):
    country = row.findAll('td')
    if len(country)==5:
        A = country[1].text.strip()
        B = country[2].text.strip()
        C = country[3].text.strip()
        D = country[4].text.strip()
        c.execute("INSERT INTO icc VALUES('{}','{}','{}','{}')".format(A,B,C,D))
    
c.execute("SELECT * FROM icc")
c.fetchall()
# commits the current transaction 
conn.commit()

# closing the connection 
conn.close()