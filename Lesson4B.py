# Loops => Sometimes, we may need to do a piece of work a number of repeated times and in such cases,we may use loops.
# A loop is a control stracture that allows us to execute a block of code repetedly until a certain condition is met.
# There are two types of loops in python i.e., the for loop and the while loop.
# Below is the syntax of the for loop in python.
"""
for variable in range(n):
     #block of code to be executed
"""

for greeting in range(50):
    print("Hello Moses.", greeting)

    print("===============================")

for number in range(10, 21):
    print(number)    

    print("================================")
# Find the even numbers in the range of 50-71.
for number in range(50, 71, 2):
    print(number)

    print("==================================")
# Create a python program that prints the odd numbers from 100-150.
for number in range(101, 150, 2):
    print(number)


    print("==================================")
# Create a program that prints the multiples of 3 starting from 201-150.
for number in range(201, 149, -1):
    if number % 3 == 0:
        print(number)

    print("==================================")
# Create a python program that prints the leap years between 2000 to 2024.
for number in range(2000, 2025):
    if number % 4 == 0:
        print(number)

    print("==================================")
for number in range(2000, 2025, 4):
    print(number)