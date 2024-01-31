class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def age(self):
        return self.year


car = Car('Volkswagen', 'Passat', '2005')
print(car.age())