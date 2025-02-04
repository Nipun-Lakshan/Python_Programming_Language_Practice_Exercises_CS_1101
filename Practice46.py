# CS 1101 - Week 11 Videos - NumPy - Practice 07

import numpy as NumPy

print()
array_a = NumPy.array([[1, 2], [3, 4]])
print(array_a)

print()
array_b = NumPy.array([[2, 2], [6, 6]])
print(array_b)

# Single - Array Operation
print()
print(array_a.sum()) # 10 (Add all elements)
print(array_a.sum(axis=0)) # (4, 6) -> axis = 0 (Column Wise)
print(array_a.sum(axis=1)) # (3, 7) -> axis = 1 (Row Wise)
print(array_a.cumsum()) # [ 1  3  6 10] // returns the cumulative sum of an array along a given axis. 1 1+2 = 3 3+3 = 6 ...
print(array_a.prod()) # 24 // returns the product of all elements in an array along a given axis.
print(array_a.cumprod()) # [ 1  2  6 24] // returns the cumulative product of an array along a given axis.

# Two - Array Math
print()
print(array_a + array_b) # Element - Wise
print(array_a - array_b) # Element - Wise
print(array_a * array_b) # Element - Wise
print(array_a / array_b) # Element - Wise
print(NumPy.dot(array_a, array_b))