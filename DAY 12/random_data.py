#importing numpy
import numpy as np

#creating random int ndarray
rand = np.random.randint(5, 15, 10)

#crerating random float ndarray
random_float_array = np.random.uniform(5, 15, size=(10))

#you can perform the same for float values also
#finding mode using counter
from collections import Counter
mode = Counter(rand).most_common(1)
print(mode)

#finding mode using scipy
from scipy import stats
mode1 = stats.mode(rand)
print(mode1)