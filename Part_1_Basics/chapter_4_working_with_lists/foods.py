# # Copying a List
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print(f"\nMy favorite foods are: \n")
# for food in my_foods:
#     print(f"{food.title()}")

# print(f"\nMy friend's favorite foods are: \n")
# for food in friend_foods:
#     print(f"{food.title()}")
# print("")

# Copying a List
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print(f"\nMy favorite foods are: \n")
for food in my_foods:
    print(f"{food.title()}")

print(f"\nMy friend's favorite foods are: \n")
for food in friend_foods:
    print(f"{food.title()}")
print("")
