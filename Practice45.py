# CS 1101 - Week 11 Videos - NumPy - Practice 06

import numpy as NumPy

print()
#array_a = NumPy.array([32766, 32767, 32768], dtype=NumPy.int16) // OverFlow Error
array_a = NumPy.array([32766, 32767, 32768], dtype=NumPy.int32)
print(array_a)
print(array_a.dtype)

print()
#array_d = NumPy.array([-1, 0, 1], dtype=NumPy.uint16) // UnderFLow Error
array_d = NumPy.array([-1, 0, 1], dtype=NumPy.int8)
print(array_d)
print(array_d.dtype)
'''
==========
Data Types
==========

(A) Signed Integers

01. NumPy.int16 Integer => (-32768 to 32767)
02. NumPy.int32 Integer => (-2147483648 to 2147483647)
03. NumPy.int64 Integer => (-9223372036854775808 to 9223372036854775807)

(B) Unsigned Integers

01. NumPy.uint16 Unsigned Integer => (0 to 65535)
02. NumPy.uint32 Unsigned Integer => (0 to 4294967295)
03. NumPy.uint64 Unsigned Integer => (0 to 18446744073709551615)

(C) Floating - Point Numbers

# NumPy.float same as Pythons

'''
