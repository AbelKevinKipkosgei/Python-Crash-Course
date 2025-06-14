def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print(f"\nPlease tell me your name: ")
    print(f"(Enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name.lower() == "q":
        break

    m_name = input("Middle name: ")
    if m_name.lower() == "q":
        break

    l_name = input("Last name: ")
    if l_name.lower() == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name, m_name)
    print(f"\n Hello, {formatted_name}!")
