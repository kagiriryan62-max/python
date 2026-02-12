# Create a oython program that is able to determine whether a number enetered is an odd number or an even number.
# number = int(input("Enter your number here:"))
# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person. If the weight is greater than 50KGs and age is above, he can be able to donate blood, else, not possible.

age = int(input("Enter your age here: "))
weight = float(input("Enter your weight here: "))

if age >= 18 and weight > 50:
    print("Can donate")
else:
    print("Not possible")