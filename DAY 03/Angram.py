num=int(input("Enter number of test cases : "))
for alpha in range(0,num):
    s1=input()
    s2=input()
    d=0
    m=len(s1)+len(s2)
    l1=set(s1).intersection(set(s2))
    for i in l1:
        d=d+min(s1.count(i),s2.count(i))
    x=m-2*d
    if x ==0:
        print("Angram")
    else:
        print("Not Angram")
    
    
user_input=input("Enter text : ")
user_input1=input("Enter text : ")
res={}
res1={}
for keys in user_input:
    res[keys]=res.get[keys,0]+1
for keys in user_input1:
    res1[keys]=res1.get[keys,0]+1
if res==res1:
    print("Angram")
else:
    print("NotAngram")