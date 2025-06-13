def make_car(manufacturer, model, **car_info):
    """Build a car info dictionary."""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model

    return car_info


car = make_car("ford", "raptor", color="grey", lift_gate=True)
print(car)
car1 = make_car("ram", "trx", color="black", rear_wheel_driver=True)
print(car1)
car2 = make_car(
    "dodge", "hell cat", horsepower=1000, transmission="6 speed automatic gear box"
)
print(car2)
