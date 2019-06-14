import string
def ispangram(str): 
    lst = list(string.ascii_lowercase)
    for x in lst: 
        if x not in str.lower(): 
            return False
  
    return True
      
string1 = input("Enter your text here : ")
if(ispangram(string1) == True): 
    print("Pangram") 
else: 
    print("Not Pangram") 