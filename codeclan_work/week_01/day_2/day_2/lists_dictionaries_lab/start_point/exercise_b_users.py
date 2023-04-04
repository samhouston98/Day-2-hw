users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

twitter_handle = users["Jonathan"]["twitter"]
print(twitter_handle)

# 2. Get Erik's hometown

home = users["Erik"]["home_town"]
print(home)

# 3. Get the list of Erik's lottery numbers

lottery = users["Erik"]["lottery_numbers"]
print(lottery)

# 4. Get the species of Avril's pet Monty

pet_species = users["Avril"]["pets"][0]
print(pet_species)

# 5. Get the smallest of Erik's lottery numbers

smallest = sorted(users["Erik"]["lottery_numbers"])[0]
print(smallest)

# 6. Return a list of Avril's lottery numbers that are even

lottery_numbers = users["Avril"]["lottery_numbers"]
even_numbers=[]
for number in lottery_numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

lottery = users["Erik"]["lottery_numbers"]
lottery.append(7)
print(lottery)


# 8. Change Erik's hometown to Edinburgh

# town = users["Erik"]["home_town"]
# town.remove("Linlithgow")
# town.append("Edinburgh")
# print(town)

users["Erik"]["home_town"] = "Edinburgh"


# 9. Add a pet dog to Erik called "fluffy"

users["Erik"]["pets"] = "fluffy"
print(users)


# 10. Add another person to the users dictionary



print(users)