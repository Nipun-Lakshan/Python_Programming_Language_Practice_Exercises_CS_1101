# CS 1101 - Week 09 - Video 18 - Tuples

numbers = (1, 2, 3)
# numbers[0] = 10 -> Tuples are immutable. So the syntax caused the error.
numbers = (1, 2, 3, 3)
print(numbers.count(3))  # 2
print(numbers.index(1))  # 0
# () -> Empty Tuple
