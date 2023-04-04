empty_dictionary = {}
other_empty_dictionary = dict()

car = {
    "make": "ford",
    "model": "fiesta",
    "engine_size":  1300,
    "colour:": "red",
    "engine:
        "make": "acme"}"passengers": []


print(car["model"])
print(car.get("fuel_type", "no fuel specified"))

has_a_fuel_type = "fuel_type" in car
print(has_a_fuel_type)

car["colour"] = "green"
car["length"] = 2

print(car)

del car["engine_size"]
print(car)

print(car.keys())
print(list(car))
print(car.values())


engine_make = car["engine"]["make"]