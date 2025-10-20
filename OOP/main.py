class Car:
    def __init__(self, make, model): # constructor
        self.make = make
        self.model = model
    
    def origin(self):
        return f"{self.make} is from Japan"
    

# object
car_one = Car("Toyota", "Hilux")

print(car_one.make)
print(car_one.origin())