from  selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as BS

#taking input
sign = input("Enter your Year")
sign1 = input("Enter your Month")
sign2 = input("Enter your Date")
A=[]

#opening browser
url = "https://www.astrology.com/horoscope/daily.html"
browser = webdriver.Chrome("C:/Users/MY HP/Desktop/FSDP2019/DAY 08/chromedriver.exe")
browser.get(url)


sleep(2)
#month input
select = Select(browser.find_element_by_name("MonthSelector"))
code1 = sign1

sleep(3)
select.select_by_visible_text(code1)


sleep(2)
#date input
select = Select(browser.find_element_by_name("DaySelector"))
code2 = sign2

sleep(3)
select.select_by_visible_text(code2)


sleep(2)
#year input
select = Select(browser.find_element_by_name("YearSelector"))
code = sign

sleep(3)
select.select_by_visible_text(code)

sleep(2)

filter_ = browser.find_element_by_xpath('/html/body/section[1]/form/div/button')
filter_.click()

sleep(5)

copy = browser.find_element_by_xpath('/html/body/section/section[1]/div[2]/main/p').text
A.append(copy)

from collections import OrderedDict

col_name = ["Your Horoscope"]
col_data = OrderedDict(zip(col_name,[A]))

import pandas as pd
df = pd.DataFrame(col_data)
df.to_csv("Horoscope.csv")