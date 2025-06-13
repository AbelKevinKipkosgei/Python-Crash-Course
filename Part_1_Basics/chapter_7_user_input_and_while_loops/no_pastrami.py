sandwich_orders = [
    "philly cheesesteak",
    "pastrami",
    "tuna melt",
    "caprese",
    "pastrami",
    "croque monsieur",
    "grilled cheese",
    "pastrami",
]

print(f"\nDeli has run out of Pastrami.\n")

# Remove all pastrami
finished_sandwiches = []
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Process remaining orders
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f"I made your {made_sandwich.title()}.")
    finished_sandwiches.append(made_sandwich)

print(f"\nSandwiches made include: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")
