lst=[]
Sum=0
str1=[]
n = int(input("Enter number of elements : ")) 
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
lst.append(0)
for n, i in enumerate(lst):
    if i == 13:
        lst[n+1]=0
        lst[n]=0
for i in lst:
    Sum=Sum+i
Sum
            