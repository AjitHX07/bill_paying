import random

seedtest = input("enter a numer")
random.seed(seedtest)

input_name = input("enter name in ',' to saparate")
name = input_name.split(",")


len_name = len(name)


whopay = random.randint(0, len_name-1)

whopay1 = name[whopay]
print(whopay1)
