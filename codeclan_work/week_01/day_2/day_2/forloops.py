
numbers = [1,2,3,4,5]
names = ("Ben", "Sam", "Bruce")
chickens = [
    { "name" : "Margaret", "age": 2, "eggs": 0},
    { "name" : "Tony", "age": 8, "eggs": 9}
    
]

for number in numbers:
    print(number * 2)

for name in names:
    print(name)

total_eggs = 0

for chicken in chickens:
    print(f"{chicken['name']} is {chicken['age']}")
    total_eggs += chicken['eggs']

print(f"total eggs: {total_eggs}")

