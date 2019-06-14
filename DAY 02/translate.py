consonants = 'bcdfghjklmnpqrstuvwxyz'
newtext = []
new=""
mytext=input("Enter your code here : ")
for i in mytext:
    if i not in consonants:
        newtext.append(i)
    else:
        newtext.append(i)
        newtext.append('o')
        newtext.append(i)

for x in newtext:
    new+=x
print(new)