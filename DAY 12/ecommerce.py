#importing recquired 
import numpy as np
import matplotlib.pyplot as plt

#creating random nmbers
incomes = np.random.normal(100.0, 20.0, 10000)
#finding mean value
print("Mean value is: ", np.mean(incomes))
#finding median
print("Median value is: ", np.median(incomes))
#plotting histo graph with 50 bars
plt.hist(incomes, 50)
plt.show()