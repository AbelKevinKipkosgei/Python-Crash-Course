# # Pizzas
# pizzas = ['margherita', 'pepperoni', 'neapolitan', 'hawaiian']
# for pizza in pizzas:
#     print(f"\nI like {pizza.title()} pizza.\n")
# print(f"I really love pizza!\n")

# # My Pizzas, Your Pizzas
# friend_pizzas = pizzas[:]

# pizzas.append('calzone')
# friend_pizzas.append('stromboli')

# print(f"My favorite pizzas are: \n")
# for pizza in pizzas:
#     print(f"{pizza.title()}")

# print(f"\nMy friend's favorite pizzas are: \n")
# for pizza in friend_pizzas:
#     print(f"{pizza.title()}")

# # Animals
# animals = ['dog', 'parrot', 'cat', 'horse']
# for animal in animals:
#     print(f"\nA {animal.lower()} would make a great pet.\n")
# print(f"\nAny of these animals is highly intelligent.\n")

# # Counting to Twenty
# for value in range(1, 21):
#     print(value)

# # # One Million
# # million = [number for number in range(1, 1000001)]
# # print(million)

# # # Summing a Million
# # one_million = [digit for digit in range(1, 1000001)]
# # print(f"\nMinimum : {min(one_million)}")
# # print(f"\nMaximum : {max(one_million)}")
# # print(f"\nSum : {sum(one_million)}\n")

# # Odd Numbers
# odd_numbers = [odd_number for odd_number in range(1, 20, 2)]
# print(f"{odd_numbers}\n")

# # Threes
# threes = [three for three in range(3, 31, 3)]
# print(f"{threes}\n")

# # Cubes
# cubes = []
# for cube in range(1, 11):
#     cubes.append(cube ** 3)
# print(f"{cubes}\n")

# # Cube comprehension
# cubes_list = [cubed ** 3 for cubed in range(1, 11)]
# print(f"{cubes_list}\n")

# # Slices
# print(f"The first three items in the cubes list are: \n\n{cubes_list[:3]}\n")

# middle_index = len(cubes_list) // 2
# start_index = middle_index - 1
# end_index = middle_index + 2

# print(f"The three items from the middle of the cubes list are: \n\n{cubes_list[start_index:end_index]}\n")

# third_last_index = len(cubes_list) - 3

# print(f"The last three items in the cubes list are: \n\n{cubes_list[third_last_index:]}\n")

# # Buffet
# buffet = ('rice', 'pizza', 'pasta', 'beans', 'omelette')
# print(f"Original menu:")
# for food in buffet:
#     print(food)

# buffet = ('pilau', 'pizza', 'pasta', 'peas', 'omelette')
# print(f"\nRevised menu:")
# for food in buffet:
#     print(food)

# Pizzas
pizzas = ["margherita", "pepperoni", "neapolitan", "hawaiian"]
for pizza in pizzas:
    print(f"\nI like {pizza.title()} pizza.\n")
print(f"I really love pizza!\n")

# My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]

pizzas.append("calzone")
friend_pizzas.append("stromboli")

print(f"My favorite pizzas are: \n")
for pizza in pizzas:
    print(f"{pizza.title()}")

print(f"\nMy friend's favorite pizzas are: \n")
for pizza in friend_pizzas:
    print(f"{pizza.title()}")

# Animals
animals = ["dog", "parrot", "cat", "horse"]
for animal in animals:
    print(f"\nA {animal.lower()} would make a great pet.\n")
print(f"\nAny of these animals is highly intelligent.\n")

# Counting to Twenty
for value in range(1, 21):
    print(value)

# # One Million
# million = [number for number in range(1, 1000001)]
# print(million)

# # Summing a Million
# one_million = [digit for digit in range(1, 1000001)]
# print(f"\nMinimum : {min(one_million)}")
# print(f"\nMaximum : {max(one_million)}")
# print(f"\nSum : {sum(one_million)}\n")

# Odd Numbers
odd_numbers = [odd_number for odd_number in range(1, 20, 2)]
print(f"{odd_numbers}\n")

# Threes
threes = [three for three in range(3, 31, 3)]
print(f"{threes}\n")

# Cubes
cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)
print(f"{cubes}\n")

# Cube comprehension
cubes_list = [cubed**3 for cubed in range(1, 11)]
print(f"{cubes_list}\n")

# Slices
print(f"The first three items in the cubes list are: \n\n{cubes_list[:3]}\n")

middle_index = len(cubes_list) // 2
start_index = middle_index - 1
end_index = middle_index + 2

print(
    f"The three items from the middle of the cubes list are: \n\n{cubes_list[start_index:end_index]}\n"
)

third_last_index = len(cubes_list) - 3

print(
    f"The last three items in the cubes list are: \n\n{cubes_list[third_last_index:]}\n"
)

# Buffet
buffet = ("rice", "pizza", "pasta", "beans", "omelette")
print(f"Original menu:")
for food in buffet:
    print(food)

buffet = ("pilau", "pizza", "pasta", "peas", "omelette")
print(f"\nRevised menu:")
for food in buffet:
    print(food)
