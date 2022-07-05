class coffeeShop:
    def __init__(self, name, location, hours, wifi, bathrooms, price_level):
        self.name = name
        self.location = location
        self.hours = hours
        self.wifi = wifi
        self.bathrooms = bathrooms
        self.price_level = price_level

    def __str__(self):
        return f"(Coffee Shop: {self.name} located in {self.location})"


starbucks = coffeeShop('Starbucks', 'San Francisco, CA', '6am-6pm', True, True, 'Middle')
print(starbucks)
