from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("C:/Users/MY HP/Desktop/FSDP2019/DAY 08/chromedriver.exe")
browser.get(url)

sleep(3)

bid_code = browser.find_element_by_name("search_by")
code="GEM/2019/RA/9593"
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
