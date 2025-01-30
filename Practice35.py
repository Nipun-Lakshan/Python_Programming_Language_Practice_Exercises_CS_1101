# CS 1101 - Week 10 - Exercise 01 - Method & Function Which Related To Lists

##### Lists
months = ['January', 'February', 'March', 'April']
marks = [78, 65, 52, 90, 55]
print(months)
print(marks)
print(months[0])
print(months[1:2])
print(months[1:3])
print(months[-2])
print(months[1:3:-1])
print(months[0:3:-1])
print(str(len(marks)))
print(str(min(marks)))
print(str(max(marks)))
print(str(sum(marks)))
months.append('May')
print(months)
print(months.pop(2))
print(months)
months.insert(2, 'March')
print(months)

##### Tuples
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May')
print(months)
empty_tuple = (5, )
empty_list = []
print(empty_tuple)
print(empty_list)
mark = tuple(marks)
print(mark)
months_t2 = 'Dec', 'Nov'
print(months_t2)
a = [2, 5, 6, 7, 9, 10]
print(a)
b = a  # Both are same and only referencing
print(b)
b[-1] = 100
print(b)
print(a)
b = list(a)  # Each od Them are Separately Works
b[-1] = 25
print(b)
print(a)

##### Dictionaries
actress = {'name': 'Emma', 'age': 34, 'county': 'UK'}
print(actress)
print(type(actress))
print(actress['name'])
print(actress.keys())
print(actress.values())
actress.pop('age')
print(actress)
actress.clear()
print(actress)

##### Sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
print(union_set) # {1, 2, 3, 4, 5, 6}
print(intersection_set) # {3 , 4}
print(difference_set) # {1, 2}

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)
print(unique_elements)