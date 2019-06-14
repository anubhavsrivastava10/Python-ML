user_input = input("Enter the text : ")
dict1={}
for counter in user_input:
    dict1[counter] = dict1.get(counter, 0) +1
print(str(dict1))