# A Dictionary is a data type that stores data in terms of key-value pair.
# It is introduced by the use of carly braces {}
# The values stored inside of a dictionary can be of any data type.
# To access the values in a dictionary, we use the keys.


phonebook = {
    "Benson": "+25471234567",
    "Mary": "+2547654786",
    "Stephen": "+2547453678"
}

# Showing the entire dictionary
print(phonebook)
print(type(phonebook))

# Printing out Benson's number
print(phonebook["Benson"])

print("====================")

player = {
    "name": "Messi",
    "age": 40,
    "teams": ["Barcelona", "PSG", "Argentinna"],
    "more": {
        "children": 3,
        "residence": "US",
        "phone": (+2547123456, +2547654789, +2547243567)
    }
}
#Print the second team he played for.
print(player["teams"][1])

# Print Messi's second number.
print("The second number of Messi is:",player["more"]["phone"][1])

# Research on if...else statements in python.