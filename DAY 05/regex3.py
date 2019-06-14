import re
user_in = int(input("enter the number of credit card number you have : "))
lst=[]
lst1=[]
def leng(val):
    for i, n in enumerate(val):
            try:
                if (val[i],val[i+1],val[i+2],val[i+3]) == (n, n, n, n):
                    return False
            except IndexError:
                pass
        
for i in range(0,user_in):
    str1=input("Number : ")
    lst.append(str1)

for val in lst:
    if re.findall(r'^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$',val):
        if leng(val) == True:
            print("valid")
        else:
            print("invalid")
#you can also use this for checking 4 consecutive numbers
#(\d)\1{3,}