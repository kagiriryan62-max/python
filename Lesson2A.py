#Python Lists
# A list in python is a collection of items that are ordered in a certain way.
# A list is introduced by the use of the square brackets ({})
# The items of a list are stored inside of indexes. Note: In programing, we start counting from index '0'.
# A list is mutable i.e., the contents of a list can be changed.
cars = ["BMW", "Benz", "KIA", "Probox", "Hiance", "Mclaren", "Prado", "Range"]
print(cars)
print(type(cars))

# Accessing items of a list.
print(cars[2])
print(cars[3])

# List slicing- This is creating a list from a given bigger list.
print(cars[3:])
print(cars[0:4])

# Printing from KIA to Hiance
print(cars[2:5])

# List mutability
# We use the function append to add an item at the end of a list.
cars.append("Escalade")
print(cars)
cars.append("Subaru")
print(cars)

# We use the pop function to remove an item at the end of the list.
cars.pop()
print(cars)

# We can use an index to add an item to a list.
cars[5] = "Pajero"
print(cars)

# We can use the sort function to sort our items in alphabetical order.
cars.sort()
print(cars)

del cars[4]
print(cars)

cars.pop(4)
print(cars)

cars.remove("BMW")
print(cars)