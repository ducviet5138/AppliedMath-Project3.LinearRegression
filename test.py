import numpy as np

x = np.array([2, 2, 2])
expo = np.array([1, 2, 3])
mask = np.array([True, False, True])

print(np.power(x[mask], expo[mask]))