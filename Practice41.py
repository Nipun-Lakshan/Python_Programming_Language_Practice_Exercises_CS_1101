# CS 1101 - Week 11 Videos - NumPy - Practice 02

import numpy as NumPy

# Creating 3 x 3 Matrix
seq_a = [1, 2, 3]
seq_b = [4, 5, 6]
seq_c = [7, 8, 9]

print()
array_abc = NumPy.array([seq_a, seq_b, seq_c])
print(array_abc)
print(array_abc.shape)  # (3, 3)

print()
seq_d = [10, 11, 12]
array_abc = NumPy.array([seq_a, seq_b, seq_c, seq_d])
print(array_abc)
print(array_abc.shape)  # (4, 3)

print()
seq_d = [10.5, 11.5, 12.5]
array_abc = NumPy.array([seq_a, seq_b, seq_c, seq_d])
print(array_abc)
print(array_abc.shape)

print()
array_d = NumPy.array([[]])
print(array_d)
print(array_d.shape) # (1, 0)