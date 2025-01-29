# CS 1101 - Week 10 - Practice 03

# Code 01
string_1 = "Simple Learn"
string_2 = "Tim's Birthday"
string_3 = 'Tim said, "I am busy today!"'
string_4 = '''Tim said, "I'm busy Today"'''
string_5 = "Tim said, \"I'm busy Today\""
string_6 = '''Hey there!
Welcome to Simply Learn'''
print("\n" + string_1)
print(string_2)
print(string_3)
print(string_4)
print(string_5)
print(string_6)

# Code 02
print('Length of "Simply Learn" : ' + str(len('Simply Learn')))
print(string_1[5])  # e
for i in reversed(range(0, len(string_1))):
    print(string_1[i])
for i in range(0, len(string_1)):
    print(string_1[i], end="")
print("\n")
print(string_1[0:5])
print(string_1[:5])
print(string_1[5:])
print(string_1[2:5])
print()

# Code 3
string = "Welcome to Simple Learn"
print(string.upper())
print(string.lower())
print(string.find('S'))  # 11
print(string.index('S'))  # 11
x = string.split(" ")  # ['Welcome', 'to', 'Simple', 'Learn']
print(x)
print(string.replace("Welcome", "You have"))
Y = string.rpartition(" to ")  # Give Tuple with 3 Elements
print(Y)  # Y = ('Welcome', ' to ', 'Simple Learn')

# Code 04
s1 = "Good"
s2 = "Morning!"
s3 = s1 + " " + s2
print(s3)
print(s1 + " " + s2)

# Code 05
s1 = "Hey"
s2 = "there,"
s3 = "All"
s4 = "{} {} {}!".format(s1, s2, s3)
print(s4)

# Exercise - Reverse Each Word in Any Sentence
user_input = input("Enter any Sentence : ")
user_input_modified = user_input + " "
temp = ""
rev = ""

for i in user_input_modified:
    if i != " ":
        temp = i + temp
    else:
        rev = rev + temp + " "
        temp = ""
print(rev)
