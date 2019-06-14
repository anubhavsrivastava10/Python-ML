from bs4 import BeautifulSoup   
import requests
from collections import OrderedDict


icc = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(icc).text
soup = BeautifulSoup(source,"lxml")
print (soup.prettify())
right_table=soup.find('table', class_='table')
print (right_table.prettify())

A=[]
B=[]
C=[]
D=[]

for row in right_table.findAll('tr'):
    country = row.findAll('td')
    if len(country)==5:
        A.append(country[1].text.strip())
        B.append(country[2].text.strip())
        C.append(country[3].text.strip())
        D.append(country[4].text.strip())
    
    
col_name = ["Country Name","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D]))

import pandas as pd
df = pd.DataFrame(col_data)
df.to_csv("former.csv")