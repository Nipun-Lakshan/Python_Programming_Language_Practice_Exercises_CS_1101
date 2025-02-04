# CS 1101 - Week 11 Videos - NumPy - Practice 04

import numpy as Numpy

print()
array_a = Numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
                       [13, 14, 15, 16]])
print(array_a)
print(array_a.shape)
print(array_a.size)

print()
array_b = array_a.reshape(1, 16)
print(array_b)
array_b = array_a.reshape(4, 4)
print(array_b)
array_b = array_a.reshape(8, 2)
print(array_b)
array_b = array_a.reshape(16, 1)
print(array_b)

print()
array_b = array_a.reshape(2, 8)
print(array_b)

print()
array_c = array_a.T
print(array_c)
print(array_c.T)
print(array_c[0])
print(array_c[0, 1])
print(array_c[0], array_c[1])
print(array_a[0, -1])
print(array_a[-1, -1])
print(array_a[:, -3])
