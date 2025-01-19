# CS 1101 - Week 09 - Video 14 - Lists
'''
Data Types
==========

- Numbers [Integers / Float]
- Booleans [Integer / Float]
- Strings ["Mosh"]
- List -> ["Jon", "Mary", "Jupiter"]

Indexes
=======

-1 -> Last Element
-2 -> Element Before Last Element
0  -> First Element
'''
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)  # ['John', 'Bob', 'Mosh', 'Sam', 'Mary']
print(names[0])  # John
print(names[-1])  # Mary
print(names[-2])  # Sam
names[0] = 'Jon'
print(names)  # ['Jon', 'Bob', 'Mosh', 'Sam', 'Mary']
print(names[0:3])  # ['Jon', 'Bob', 'Mosh']
names[-1] = True
print(names)  # ['Jon', 'Bob', 'Mosh', 'Sam', True]
