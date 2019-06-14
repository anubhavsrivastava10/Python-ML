import re

user_in = int(input("enter the number of emails you want to enter : "))
lst=[]
lst1=[]
for i in range(0,user_in):
    str1=input("Email : ")
    lst.append(str1)

for val in lst:
    if re.match(r'[a-zA-z0-9_-]+\@+[a-zA-Z0-9]+\.+[a-z]{2,4}$',val):
        lst1.append(val)

sorted(lst1)