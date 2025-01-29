# CS 1101 - Week 10 - Practice 04 - Functions


def first_func():
    print("We did it!")


first_func()


def number_squared(number):
    print(number**2)


number_squared(5)


def number_squared_cust(number, power):
    print(number**power)


number_squared_cust(5, 3)  #125

args_tuple = (5, 6, 1, 2, 8)


def number_args(*number):  # Don't Know the Limit of Arguments
    print(number[0] * number[1])


number_args(*args_tuple)  # Inserting Arguments as Tuple

number_squared_cust(power=5, number=3)


def number_kwarg(**number):
    print("My number : " + number['integer1'] + ". My Other Number : " +
          number['integer2'] + ".")


number_kwarg(integer1='2309', integer2='349')
