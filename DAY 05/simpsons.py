import re
lst=[]
with open('simpsons_phone_book.txt',mode ='rt') as file:
    file_content=file.readlines()
x= 'hello'
for item in file_content:    
    if re.search(r'^[J][a-z]+\s+Neu',item):
        item=item.replace('\n','')
        lst.append(item)
lst