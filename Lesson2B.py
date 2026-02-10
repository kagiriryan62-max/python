# Tuple
# It is an imutable type of a list (It cannot change)
# To introduce a tuple, we use the parenthesis ()

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")
print(counties)
print(type(counties))

# Slicing of tuples
print(counties[3:])

# Accessing items of a tuple by the use of an index.
print(counties[5])

# Note: Below you will generate an error.
# Attribute error.
counties.append("Machakos")
print(counties)

