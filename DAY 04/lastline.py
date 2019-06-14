try:
    file = open(input("Enter File Name : "),  "rt" )
    print (file.name)
except IOError:
    print ( "File not Found or incorrect path")
lines = file.read().splitlines()
last_line = lines[-1]
print (last_line)