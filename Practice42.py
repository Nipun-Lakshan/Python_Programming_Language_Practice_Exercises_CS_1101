# CS 1101 - Week 11 Videos - NumPy - Practice 03

import numpy as NumPy

print()
array_a = NumPy.array([[1, 2, 3], [4, 5, 6]])
print(array_a)
print(array_a.shape)  # (2, 3)
print(array_a.size)  # rows x columns = 2 x 3 = 6

print()
array_b = array_a.reshape(1, 6)  # Reshape
print(array_b)
array_b = array_a.reshape(
    3, 2
)  # (3, 3) gives mismatch error due to exceeding of the size of the array.
print(array_b)

print()
array_b = array_a.T  # Transpose
print(array_b)
print(array_b[0])  # First Row
print(array_b[:, 0])  # All Rows and First Column
print(array_b[0, 0])  # First Row First Column Element
