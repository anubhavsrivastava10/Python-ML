
from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

import mysql.connector
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='sql123_123', password='anubhav123',host='db4free.net', database = 'data123base')
#, database = 'forsk_test'

# creating cursor
c = conn.cursor()

#c.execute("DROP TABLE student;")

c.execute ("""CREATE TABLE student2(
          Bid_NO TEXT,
          Item TEXT,
          Quantity_Recq TEXT,
          Dep_Name TEXT,
          Start TEXT, 
          End TEXT
          )""")


url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("C:/Users/MY HP/Desktop/FSDP2019/DAY 08/chromedriver.exe")
browser.get(url)

sleep(5)

for i in range(1,11):
    gem_code = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[1]/p[1]/a''').text
    gem_item = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[1]/span''').text
    gem_quant = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[2]/span''').text
    gem_add = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[3]/p[2]''').text
    gem_start = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[1]/span''').text
    gem_end = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[2]/span''').text
    c.execute("INSERT INTO student2 VALUES('{}','{}','{}','{}','{}','{}')".format(gem_code,gem_item,gem_quant,gem_add,gem_start,gem_end))
    

c.execute("SELECT * FROM student2")
c.fetchall()
# commits the current transaction 
conn.commit()


# STEP 7
# closing the connection 
conn.close()
