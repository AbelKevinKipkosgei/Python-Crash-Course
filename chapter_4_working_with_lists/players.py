# # Slicing
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(f"\n{players[0:3]}\n")
# print(f"{players[1:4]}\n")
# print(f"{players[:4]}\n")
# print(f"{players[2:]}\n")
# print(f"{players[-3:]}\n")
# print(f"{players[::2]}\n")
# print(f"{players[::-1]}\n")

# # Looping through a slice
# print(f"Here are the first three players on my team: \n")
# for player in players[:3]:
#     print(f"{player.title()}\n")

# Slicing
players = ["charles", "martina", "michael", "florence", "eli"]
print(f"\n{players[0:3]}\n")
print(f"{players[1:4]}\n")
print(f"{players[:4]}\n")
print(f"{players[2:]}\n")
print(f"{players[-3:]}\n")
print(f"{players[::2]}\n")
print(f"{players[::-1]}\n")

# Looping through a slice
print(f"Here are the first three players on my team: \n")
for player in players[:3]:
    print(f"{player.title()}\n")
