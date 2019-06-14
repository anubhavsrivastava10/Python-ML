from functools import reduce

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

lst=[]
for char in people:
    if 'height' in char:
        lst.append(char['height'])
                        
            
def add(x,y):
    return x+y

def avg(x):
    return reduce(add,lst)/2













#my_filter_list = filter(lambda x: lst.append(char['height'] if 'height' in char for char in people), people)