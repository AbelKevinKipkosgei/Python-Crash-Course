# # Checking for a special item
# requested_toppings = ['mushrooms','green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print(f"Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}")

# print(f"Finished making your pizza!")

# # Checking that a list is not empty
# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"\nAdding {requested_topping}")
#     print(f"\nFinished making your pizza!")
# else:
#     print(f"\nAre you sure you want a plain pizza?")

# # Using multiple lists
# available_toppings = ['mushrooms','olives','green peppers', 'pepperoni',
#                       'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"\nAdding {requested_topping}.")
#     else:
#         print(f"\nSorry, we don't have {requested_topping}.")
# print(f"\nFinished making your pizza!")

# Checking for a special item
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print(f"Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

print(f"Finished making your pizza!")

# Checking that a list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"\nAdding {requested_topping}")
    print(f"\nFinished making your pizza!")
else:
    print(f"\nAre you sure you want a plain pizza?")

# Using multiple lists
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"\nAdding {requested_topping}.")
    else:
        print(f"\nSorry, we don't have {requested_topping}.")
print(f"\nFinished making your pizza!")
