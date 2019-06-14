vowel=['a','e','i','o','u']
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
newList = []
new=[]
for state in state_name:
    newList.append(state.lower())
#print(newList)
for state in newList:
    for x in state:
        if x in vowel:
            st=state.replace(x,"")
    new.append(st.lower())
print(new)