user_input = input("Enter the string : ")
import re
lst=[]
lst= user_input.split(" ")
for val in lst:
    if re.findall(r'[+-.]?\d?\.\d?',val):
        print('yes')
    else:
        print('false')