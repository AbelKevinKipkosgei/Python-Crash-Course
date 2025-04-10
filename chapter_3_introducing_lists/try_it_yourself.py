names = ['Sam', 'Marvin', 'Terry', 'Christine']
print(f"{names[0]}\n{names[1]}\n{names[2]}\n{names[3]}")
message1 = f"Hello {names[0]}, wanna learn some Python?"
message2 = f"Hello {names[1]}, wanna learn some Python?"
message3 = f"Hello {names[2]}, wanna learn some Python?"
message4 = f"Hello {names[3]}, wanna learn some Python?"
print(f"{message1}\n{message2}\n{message3}\n{message4}")
modes_of_transportation = ['car', 'motorcycle', 'train', 'airplane']
message1 = f"I would love to own a sports {modes_of_transportation[0]}."
message2 = f"The KTM 1390 Super Duke is my favorite ADV {modes_of_transportation[1]}."
message3 = f"China has the fastest levitating magnetic {modes_of_transportation[2]}."
message4 = f"I'll soon own a gulf stream jet {modes_of_transportation[3]}."
print(f"{message1}\n{message2}\n{message3}\n{message4}")
# Guest List
guest_list = ['Abel', 'Sam', 'Vivian', 'Chen', 'Suarez']
message1 = f"Welcome for dinner, {guest_list[0]}!"
message2 = f"Welcome for dinner, {guest_list[1]}!"
message3 = f"Welcome for dinner, {guest_list[2]}!"
message4 = f"Welcome for dinner, {guest_list[3]}!"
message5 = f"Welcome for dinner, {guest_list[4]}!"
print(f"{message1}\n{message2}\n{message3}\n{message4}\n{message5}")
# Changing Guest List
if "Vivian" in guest_list:
    index = guest_list.index("Vivian")
    print(f"{guest_list[index]} won't be joining us for dinner")
    guest_list[index] = "Cynthia"
    print(f"However, {guest_list[index]} will be joining us instead.")
message1 = f"Welcome for dinner, {guest_list[0]}!"
message2 = f"Welcome for dinner, {guest_list[1]}!"
message3 = f"Welcome for dinner, {guest_list[2]}!"
message4 = f"Welcome for dinner, {guest_list[3]}!"
message5 = f"Welcome for dinner, {guest_list[4]}!"
print(f"{message1}\n{message2}\n{message3}\n{message4}\n{message5}")
# More Guests
print(f"Hello guys I just got a bigger dinning table.")
first_new_guest = guest_list.insert(0, "Lopez")
middle_index_number = len(guest_list) // 2
second_new_guest = guest_list.insert(middle_index_number, "Bradford")
last_new_guest = guest_list.append("Harper")
message1 = f"Welcome for dinner, {guest_list[0]}!"
message2 = f"Welcome for dinner, {guest_list[1]}!"
message3 = f"Welcome for dinner, {guest_list[2]}!"
message4 = f"Welcome for dinner, {guest_list[3]}!"
message5 = f"Welcome for dinner, {guest_list[4]}!"
message6 = f"Welcome for dinner, {guest_list[5]}!"
message7 = f"Welcome for dinner, {guest_list[6]}!"
message8 = f"Welcome for dinner, {guest_list[7]}!"
print(f"{message1}\n{message2}\n{message3}\n{message4}\n{message5}\n{message6}\n{message7}\n{message8}")
# Shrinking Guest List
print(f"I'm sorry but I can only host two people for dinner.")
while len(guest_list) > 2:
    message = f"I'm sorry {guest_list.pop()}, but I can only host two people for dinner."
    print(message)
    print(guest_list)

for guest in guest_list:
    message = f"Hello {guest}, you're still invited for dinner."
    print(message)
print(f"{len(guest_list)} guests have been invited for dinner.")
# Removing Guests
del guest_list[0:]
print(guest_list)
# Seeing the World
travel_destinations = ['maldives', 'abu dhabi', 'vienna', 'istanbul', 'cairo']
print("\nOriginal travel destinations: ")
print(travel_destinations)
print("\nTemporarily sorted travel destinations: ")
print(sorted(travel_destinations))
print("\nOriginal travel destinations again: ")
print(travel_destinations)
print("\nTemporarily sorted travel destinations in reverse order: ")
print(sorted(travel_destinations, reverse=True))
print("\nOriginal travel destinations after sorting and reversing: ")
print(travel_destinations)
print("\nPermanently reversed travel destinations: ")
travel_destinations.reverse()
print(travel_destinations)
print("\nTravel destinations reversed again to original format: ")
travel_destinations.reverse()
print(travel_destinations)
print("\nPermanently sorted travel destinations: ")
travel_destinations.sort()
print(travel_destinations)
print("\nPermanently sorted and reversed travel destinations: ")
travel_destinations.sort(reverse=True)
print(travel_destinations)