# CS 1101 - Week 09 - Video 07 - Strings

course = "Python For Beginners"
print("")
print(course.upper())  # Upper Case
print((course.upper()).lower())  # Lower Case
print(course.find("y"))  # 1
print(course.find("Y"))  # -1 (Not Found)
print(course.find("for"))  # 7
print(course.replace("For", "4"))  # Python 4 Beginners
print(course.replace("x", "4"))  # Python For Beginners
print(course.find("Python"))  # 0
print("Python\n" in course)
