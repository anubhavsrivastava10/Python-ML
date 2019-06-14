# Taking multiple input from user
list1 = []
number = int(input("Enter number of input : "))
for x in range(0,number):
    user_input = int(input("Enter values >"))
    #append this entry to other data structure
    list1.append(user_input)
lst=[]
for num in list1:
    if num not in lst:
        lst.append(num)
print(lst[::-1])