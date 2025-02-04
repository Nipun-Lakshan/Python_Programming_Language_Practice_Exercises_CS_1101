# CS 1101 - Week 11 Videos - NumPy - Practice 08

import numpy as np

print()
array_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array_a)

print()
array_b = np.array([[2, 2, 2], [3, 4, 5], [6, 7, 8]])
print(array_b)

print()
print(array_a.sum(axis=0))  # Column Wise [12 15 18]
print(array_a.sum(axis=1))  # Row Wise    [ 6 15 24]

print()
# print(array_a.ptp(axis=1))  # Row Wise Range (max - min) # [2 2 2] -> Old Version Not Working after 2.0
print(np.ptp(array_a, axis=1))  # Row Wise Range (max - min) # [2 2 2]
print(np.ptp(array_a))  # 9 - 1 = 8

print()
print(array_a.min())  # 1
print(array_a.max())  # 9
print(array_a.mean())  # 5.0

print()
print(array_a.min(axis=1))  # [1 4 7]
print(array_a.max(axis=1))  # [3 6 9]
print(array_a.mean(axis=1))  # [2. 5. 8.]

print()
print(np.power(array_a, array_b))  # Element Wise

print()
array_c = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(array_c)

print()
print(array_a + array_b + array_c)
print(array_a / array_b / array_c)