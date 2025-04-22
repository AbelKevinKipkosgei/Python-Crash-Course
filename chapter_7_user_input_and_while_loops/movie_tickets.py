prompt = "\nPlease enter your age in years: "
prompt += "\nEnter 'quit' when you are done. "

active = True
while active:
    age = input(prompt)

    if str(age).lower() == "quit":
        break
    elif int(age) < 3:
        print(f"Your ticket is free!")
    elif int(age) >= 3 and int(age) <= 12:
        print(f"Your ticket is $10.")
    elif int(age) > 12:
        print(f"Your ticket is $15.")
