file  = open("romeo.txt","r")
#finding number of lines in a text file
num_lines = sum(1 for line in open('romeo.txt'))
dict1={}
for words in file.readlines():
    for ele in words.split():
        dict1[ele] = dict1.get(ele, 0) +1
print(str(dict1))
