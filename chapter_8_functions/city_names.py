def city_country(name, country):
    """Display city and country of origin."""
    formatted_city = f"{name}, {country}"
    return formatted_city.title()


while True:
    print(f"\nPlease enter a city name and country: ")
    print(f"(Enter 'q' to quit)")

    city_name = input("City name: ")
    if city_name.lower() == "q":
        break
    if city_name == "":
        print(f"City name cannot be blank!")
        break

    origin_country = input("Origin country: ")
    if origin_country.lower() == "q":
        break
    if origin_country == "":
        print(f"Origin country cannot be blank!")
        break

    formatted_city_country = city_country(city_name, origin_country)
    print(formatted_city_country)
