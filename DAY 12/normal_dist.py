#importing recquired
import numpy as np
import matplotlib.pyplot as plt
#creating random array
incomes = np.random.normal(1500, 20, 1000)
#plotting the histograph with 100 bars
plt.hist(incomes, 100)
plt.show()

#standard deviation
print("Standard Deviation is: ", np.std(incomes))
#varience
print("Standard Deviation is: ", np.std(incomes)**2)