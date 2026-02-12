# A forloop can also be used to iterate thriugh a list, a tuple or even a dictionary.

name = "Ryan"
for letter in name:
    print(letter)

    print("======================================")

for letter in name:
    if letter == "a":
        print("This is letter a")    
    else:
        print(letter)

        print("=================================")
# Below is a list of counties.
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]
print(counties)

for county in counties:
    print(county)

    print("=================================")

if "Nakuru" in counties:
    print("Nakuru present in the list")
else:
    print("Nakuru not present in the lsit")      

print("==================================")
# The for loop can also be used to iterate through a dictionary.


player = {
    "name" : "Mbappe",
    "age" : 25,
    "teams" : ["France", "Monaco", "PSG"],
    "nationality" : "French"
}

for key in player:
    print(key)
print("=========================================")
for value in player:
    print(player[value])
print("=====================================")
# Loop through the teams the player has played for.
for team in player["teams"]:
    print(team)