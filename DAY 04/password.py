dict1={}
with open("passwd",mode="rt") as file: #to open a file remove it's extension
    for line in file:
        feild = line.split(":")
        if feild[0] != '#':
            dict1[feild[0]] = dict1.get(feild[0],feild[2])
print(str(dict1))