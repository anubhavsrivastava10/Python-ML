l=[13,14,17,18,19]
Sum=0
my_dict = dict() 
intg=int(input("Enter the number of input you want to enter"))
for i in range(0,intg):
    key = input("Enter key : ")
    value = int(input("Enter key and value : "))
    my_dict[key] = value
for key,value in my_dict.items():
    if value>=13 and value<=19 and value!=15 and value!=16:
        my_dict[key]=0
for i in my_dict.values():
    Sum=Sum+i
print(Sum)