# CS 1101 - Week 09 - Video 15 - List Methods

print("a".upper())  # A
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Add One Element To The Last
print(numbers)  # [1, 2, 3, 4, 5, 6]
numbers.insert(0, 6)  # Add Element to Zero Index
print(numbers)  # [6, 1, 2, 3, 4, 5, 6]
numbers.remove(3)
print(numbers)  # [6, 1, 2, 4, 5, 6]
numbers.clear()
print(numbers)  # []
numbers = [6, 1, 2, 3, 4, 5, 6]
print(1 in numbers)  # True
print(10 in numbers)  # False
print(len(numbers))

