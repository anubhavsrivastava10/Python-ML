#taking input
str1 = input("Enter numbers (len = 9): ")
#removing spaces
str1 = list(str1.split(" "))
#converting the string list to int list
str1 = [int(i) for i in str1]
#importing numpy
import numpy as np
#converting list to ndarray
x = np.array(str1)
#reshaping the nd array
x = x.reshape(3,3)