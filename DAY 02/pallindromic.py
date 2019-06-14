def pallindrome(lst_,lst__):
    for char in lst_:
        if char not in lst__:
            return False
    return True


lst_ = [] 
lst__=[]
n = int(input("Enter number of elements : ")) 
for i in range(0, n):
    ele = int(input())
    lst_.append(ele)
for x in lst_:
    ele1=int(str(x)[::-1])
    lst__.append(ele1)
if(pallindrome(lst_,lst__) == True):
    print("Yes")
else:
    print("NO")