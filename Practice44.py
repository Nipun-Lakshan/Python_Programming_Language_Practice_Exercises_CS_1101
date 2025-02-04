# CS 1101 - Week 11 Videos - NumPy - Practice 05

import numpy as NumPy

print()
array_a = NumPy.array([[1, 2, 3], [4, 5, 6]], dtype=float)
print(array_a)

print()
array_b = NumPy.zeros((3, 3))  # 3 x 3 Matrix filled with zeros
print(array_b)

print()
array_c = NumPy.ones((3, 3))  # 3 x 3 Matrix filled with ones
print(array_c)

print()
array_d = NumPy.full((3, 3), 5)
print(array_d)  # 3 x 3 Matrix filled with five

print()
array_e = NumPy.random.random((3, 4))
print(array_e) # 3 x 4 Matrix filled with random numbers between 0 to 1
