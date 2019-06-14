from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("C:/Users/MY HP/Desktop/FSDP2019/DAY 08/chromedriver.exe")
browser.get(url)

sleep(5)
A = []
B=[]
C=[]
D=[]
E=[]
F=[]
for i in range(1,11):
    gem_code = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[1]/p[1]/a''').text
    A.append(gem_code)
    gem_item = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[1]/span''').text
    B.append(gem_item)
    gem_quant = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[2]/span''').text
    C.append(gem_quant)
    gem_add = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[3]/p[2]''').text
    D.append(gem_add)
    gem_start = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[1]/span''').text
    E.append(gem_start)
    gem_end = browser.find_element_by_xpath('''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[2]/span''').text
    F.append(gem_end)

from collections import OrderedDict
    
col_name = ["Code","Item","Quantity","Address","Start date","End date"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))

import pandas as pd
df = pd.DataFrame(col_data)
df.to_csv("former1.csv")


bid_code = browser.find_element_by_name("search_by")
code=input("Enter your Bid Number : ")
bid_code.send_keys(code)

sleep(5)

filter_ = browser.find_element_by_id("search_concept")
filter_.click()

sleep(3)

#filter_1 = browser.find_element_by_class_name("drop down menu")
browser.find_element_by_link_text("Bid/RA Number").click()
#filter_1.click('Bid/RA Number')

sleep(3)

get_bid_result = browser.find_element_by_xpath('//*[@id="exTab2"]/div[1]/div[2]/form/div/span/button')
get_bid_result.click()

sleep(4)