sandwich_orders = [
    "philly cheesesteak",
    "tuna melt",
    "caprese",
    "croque monsieur",
    "grilled cheese",
]

finished_sandwiches = []
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f"I made your {made_sandwich.title()}.")
    finished_sandwiches.append(made_sandwich)

print(f"\nSandwiches made include: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")
