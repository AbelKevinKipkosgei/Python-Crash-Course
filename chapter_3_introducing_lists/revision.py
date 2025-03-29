guest_list = ['Arnold', 'Amon', 'Abel', 'Sam', 'Nonie']
print(f"Hello {guest_list[0]}, you are welcome for dinner.")
print(f"Hello {guest_list[1]}, you are welcome for dinner.")
print(f"Hello {guest_list[2]}, you are welcome for dinner.")
print(f"Hello {guest_list[3]}, you are welcome for dinner.")
print(f"Hello {guest_list[4]}, you are welcome for dinner.")
print(f"{guest_list[0]} won't make it for dinner.")
guest_list[0] = 'Lily'
print(f"Hello {guest_list[0]}, you are welcome for dinner.")
print(f"Hello {guest_list[1]}, you are welcome for dinner.")
print(f"Hello {guest_list[2]}, you are welcome for dinner.")
print(f"Hello {guest_list[3]}, you are welcome for dinner.")
print(f"Hello {guest_list[4]}, you are welcome for dinner.")
print(f"Hey I have found a bigger table hence more room for more guests.")

# Adding new guests
guest_list.insert(0, 'Terry')
guest_list.insert(2, 'Marvin')
guest_list.append('Joseph')
print(f"{guest_list}")

# Inviting all the guests and the newly added guests
print(f"Hello {guest_list[0]}, you are welcome for dinner.")
print(f"Hello {guest_list[1]}, you are welcome for dinner.")
print(f"Hello {guest_list[2]}, you are welcome for dinner.")
print(f"Hello {guest_list[3]}, you are welcome for dinner.")
print(f"Hello {guest_list[4]}, you are welcome for dinner.")
print(f"Hello {guest_list[5]}, you are welcome for dinner.")
print(f"Hello {guest_list[6]}, you are welcome for dinner.")
print(f"Hello {guest_list[7]}, you are welcome for dinner.")
print(f"I can only invite two people for dinner.")

# Shrinking guest list
print(f"Sorry {guest_list.pop()}, you are not invited for dinner.")
print(f"Sorry {guest_list.pop()}, you are not invited for dinner.")
print(f"Sorry {guest_list.pop()}, you are not invited for dinner.")
print(f"Sorry {guest_list.pop()}, you are not invited for dinner.")
print(f"Sorry {guest_list.pop()}, you are not invited for dinner.")
print(f"Sorry {guest_list.pop()}, you are not invited for dinner.")
print(f"{guest_list}")

# Inviting the remaining guests
print(f"Hello {guest_list[0]}, you're still invited for dinner.")
print(f"Hello {guest_list[1]}, you're still invited for dinner.")

# Remove the last two guests
del guest_list[1]
del guest_list[0]
print(f"{guest_list}")