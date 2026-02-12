# Boolean.
# This is a data type that evaluates whether true or false.
#

israining = False
print(israining)
print(type(israining))

paidloan = True
print(paidloan)
print(type(paidloan))

# Comparision operators. They are used to compare two or more statements and they usually return a booloean answer (True/False).

number1 = 2
number2 = 5

print("Is number1 greater than number2?", number1 > number2)
print("Is number1 less than number2?", number1 < number2)
print("Is number1 greater or equal to number2?", number1 >= number2)
print("Is number1 less than or equal to number2?", number1 <= number2)
print("Is number1 equal to number2?", number1 == number2)
print("Is number1 not equal to number2?", number1 != number2)

# Logical operators. 
# Logical AND- It returns true if a condition/ statement evaluates to true.
print((3 > 1) and (7 > 6))

# Lodical OR
# It evaluates to true if one of the statements/conditions is true.
print((3 > 1) or (7 > 6))

# Logical NOT
# It is used to negate a statement/condition.
print(not(90 > 70))