class Car:
    def __init__(self, make, model): # constructor
        self.make = make
        self.model = model
    
    def origin(self):
        return f"{self.make} is from Japan"
    
    def __repr__(self):
        return f"make={self.make} model={self.model}"
    

# object
car_one = Car("Toyota", "Hilux")

print(car_one)
