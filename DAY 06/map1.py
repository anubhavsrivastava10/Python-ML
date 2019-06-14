import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

result = map(lambda x: random.choices(code_names) , names)
print(result)
