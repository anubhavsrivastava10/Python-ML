from collections import OrderedDict
list1 = []
od = OrderedDict()
number = int(input("Enter number of input : "))
for x in range(0,number):
    user_input = input("Enter values >")
    temp = user_input.split()
    price = temp[-1]
    item = " ".join(temp[:-1])
    od[item] = od.get(item,0) + int(price)
for k,v in od.items():
    print (k,v)