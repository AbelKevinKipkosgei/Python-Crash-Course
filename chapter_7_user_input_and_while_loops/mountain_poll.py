responses = {}

# Set flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the persons name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == "no":
        polling_active = False

# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb Mount {response.title()}.")
