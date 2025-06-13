def describe_city(name, country="Greece"):
    """Describes a city."""
    print(f"\n{name.title()} is in {country.title()}.")


describe_city(name="athens")
describe_city("nairobi", "kenya")
describe_city(country="denmark", name="copenhagen")
