def sandwich(*items):
    """Build a sandwich with as many toppings as provided."""
    print(f"A sandwich with the following items: ")
    for item in items:
        print(f"- {item}")

    return items


my_sandwich = sandwich("pretzel", "brioche", "tortillas", "croissants")
print(my_sandwich)
my_sandwich1 = sandwich("croissants", "pretzel")
print(my_sandwich1)
my_sandwich2 = sandwich("brioche", "tortillas", "croissants", "lettuce")
print(my_sandwich2)
