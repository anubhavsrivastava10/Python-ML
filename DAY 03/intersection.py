list1 = []
number = int(input("Enter number of input : "))
for x in range(0,number):
    user_input = int(input("Enter values >"))
    #append this entry to other data structure
    list1.append(user_input)
list2 = []
number = int(input("Enter number of input : "))
for x in range(0,number):
    user_input = int(input("Enter values >"))
    #append this entry to other data structure
    list2.append(user_input)
pap = list(set(list1) & set(list2))
print(pap)