prompt = "\nPlease enter the desired pizza toppings: "
prompt += "\nEnter 'quit' when you are done. "

active = True
while active:
    topping = input(prompt)
    if topping.lower() == "quit":
        break
    else:
        print(f"I will add {topping} toppings to your pizza.")
