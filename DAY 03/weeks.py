days = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
user_input=input("Enter your days here : ")
user=user_input.split(",")
tup=()
tup=tuple(user)
lst=set(user)
lst1=set(days)
print(lst | lst1) 
'''
| for union.
& for intersection.
– for difference
^ for symmetric difference
'''