# current_users = ['Abelkevin', 'Johndoe', 'Janewatkins','Laracroft', 'root']
# new_users = ['root','unhinged', 'johndoe','codkiller', 'trex']
# current_users_lower = [user.lower() for user in current_users]

# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print(f"\nUsername already taken. Please enter a new username.")
#     else:
#         print(f"\nUsername is available.")

current_users = ["Abelkevin", "Johndoe", "Janewatkins", "Laracroft", "root"]
new_users = ["root", "unhinged", "johndoe", "codkiller", "trex"]
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"\nUsername already taken. Please enter a new username.")
    else:
        print(f"\nUsername is available.")
