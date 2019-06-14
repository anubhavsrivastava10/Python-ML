text = input("Enter your text> ")
n = text.find(" ")
first = text[n+1:]
second = text[:n]
print(first,second)