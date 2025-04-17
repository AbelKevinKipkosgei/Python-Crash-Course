# Person
person1 = {
    "first_name": "Abel Kevin",
    "last_name": "Kipkosgei",
    "city": "Eldoret",
}

print(f"\nFirst Name: {person1['first_name']}")
print(f"Last Name: {person1['last_name']}")
print(f"City: {person1['city']}")

# # Favorite Numbers
# favorite_numbers = {
#     "Abel": 3,
#     "Sam": 6,
#     "Anna": 8,
#     "Julius": 4,
#     "Zubeda": 2,
# }
# print(f"\nAbel: {favorite_numbers['Abel']}")
# print(f"Sam: {favorite_numbers['Sam']}")
# print(f"Anna: {favorite_numbers['Anna']}")
# print(f"Julius: {favorite_numbers['Julius']}")
# print(f"Zubeda: {favorite_numbers['Zubeda']}")

# Glossary
glossary = {
    "string": "A collection of characters.",
    "variable": "A name that stores a value, which can be changed later in the program.",
    "loop": "A control structure that repeats a block of code as long as a condition is true.",
    "list": "An ordered collection of items which can be of any data type and is mutable.",
    "dictionary": "A collection of key-value pairs, where each key maps to a specific value.",
    "set": "A collection of unique, unordered values.",
    "tuple": "An immutable ordered collection of items.",
    "function": "A reusable block of code that performs a specific task.",
    "module": "A file containing Python code that can be imported into other scripts.",
    "exception": "An error that occurs during the execution of a program.",
    "class": "A blue print for creating objects.",
}

# Glossary 2
for term, meaning in glossary.items():
    print(f"{term.title()}: {meaning.title()}\n")

# Rivers
rivers = {"nile": "egypt", "yala": "kenya", "rufiji": "tanzania"}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Each river
print(f"")
for river in rivers.keys():
    print(f"{river.title()}")

# Each country
print(f"")
for country in rivers.values():
    print(f"{country.title()}")

# People
people = [
    {
        "first_name": "abel kevin",
        "last_name": "kipkosgei",
        "city": "eldoret",
    },
    {
        "first_name": "sam",
        "last_name": "wahinya",
        "city": "nairobi",
    },
    {
        "first_name": "grace",
        "last_name": "blessing",
        "city": "lagos",
    },
]
print(f"")

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    print(f"I am {full_name} from {person['city'].title()}.")

# Pets
pets = [
    {
        "name": "bobby",
        "type": "golden retriever",
        "owner": "joy ruth",
    },
    {
        "name": "snow",
        "type": "chihuahua",
        "owner": "terry muthoni",
    },
    {
        "name": "sophie",
        "type": "beagle",
        "owner": "sam wanjigi",
    },
    {
        "name": "cyberrus",
        "type": "belgian malinois",
        "owner": "abel kevin kipkosgei",
    },
]
print(f"")
for pet in pets:
    pet_info = f"Name: {pet['name'].title()} \nType: {pet['type'].title()} \nOwner: {pet['owner'].title()}\n"
    print(f"{pet_info}")

# Favorite Places
favorite_places = {
    "abel": ["luxembourg city", "Athens", "tokyo"],
    "sarah": ["sydney", "copenhagen"],
    "jonte": ["nairobi", "mombasa", "cape town"],
    "anna": ["texas", "new york", "london"],
    "camilla": ["mexico city"],
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"{name.title()}'s favorite places are: ")
    elif len(places) == 1:
        print(f"{name.title()}'s favorite place is: ")
    for place in places:
        print(f"\t{place.title()}\n")

# Favorite Numbers
favorite_numbers = {
    "abel": [6, 3, 1],
    "sam": [9, 5],
    "anna": [2, 7, 5, 4],
    "julius": [3],
    "zubeda": [0, 8],
}

for name, numbers in favorite_numbers.items():
    numbers_string = ", ".join(str(number) for number in numbers)
    if len(numbers) > 1:
        print(f"{name.title()}'s favorite numbers are: {numbers_string}")
    elif len(numbers) == 1:
        print(f"{name.title()}'s favorite number is: {numbers_string}")

# Cities
cities = {
    "nairobi": {
        "country": "kenya",
        "population": 5000000,
        "fact": "Referred to as the 'Silicon Savannah' due to its booming tech industry.",
    },
    "abu dhabi": {
        "country": "United Arab Emirates (UAE)",
        "population": 1600000,
        "fact": "Home to the Sheikh Zayed Grand Mosque, the biggest and most architecturally impressive mosques in the world.",
    },
    "luxembourg city": {
        "country": "luxembourg",
        "population": 135000,
        "fact": "Hosts the European Court of Justice.",
    },
}

for city_name, city_info in cities.items():
    print(f"\n{city_name.title()}: ")
    for info_key, info_value in city_info.items():
        print(f"\t{info_key.title()}: {info_value}")
