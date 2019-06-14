user_input=input("Enter your File name : ")
try:
    file = open(user_input,  "rt" )
except IOError:
    print ( "File not Found or incorrect path")

dict1={}
sum1=0
dict2={}
sum2=0
dict3={}
sum3=0
#printing Number of characters
for words in file.readlines():
    for ele in words:
        dict2[ele] = dict2.get(ele,0) +1
print("Number of characters")
for i in dict2.values():
    sum2=sum2+i
print(sum2)
#printing number of words
file = open(user_input,"rt")
for words in file.readlines():
    for ele in words.split():
        dict1[ele] = dict1.get(ele,0) +1
print("Number of Words")
print(len(dict1.values()))
print("number of Unique words")
print(len(dict1.keys()))
#printing number of lines
num_lines = sum(1 for line in open(user_input))
print("number of lines")
print(num_lines)
