names = ['Mary', 'Isla', 'Sam']
result = map(lambda x: str(hash(x)), names)
print(list(result))