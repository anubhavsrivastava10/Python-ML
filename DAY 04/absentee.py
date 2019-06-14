file = open('absentee.txt', mode='at')
lst=[]
while True:
    name = input("Enter the name : ")
    file.write(name + '\n')
        
    if not name:
        break
file.close()
file = open('absentee.txt', mode='rt')
yourResult = file.readlines()
yourResult.remove('\n')
for ele in yourResult:
    ele=ele.split('\n')
file.close()