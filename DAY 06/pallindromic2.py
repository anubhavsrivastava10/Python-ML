
def pallindrome(lst__,lst_):
    for char in lst_:
        if char not in lst__:
            lst.append('0')
        else:
            lst.append('1')

lst_=[]
lst=[]
user_input = input("Enter the values : ")
user_input = user_input.split(' ')
print(user_input)
for x in user_input:
    ele1=str(x)[::-1]
    lst_.append(ele1)
print(lst_)

pallindrome(user_input,lst_)
#makin it as bool in 0,1
bool_list = list(map(int,lst))

print(any(bool_list))