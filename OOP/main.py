class Car:
    def __init__(self, make, model): # constructor
        self.make = make
        self.model = model
    
    def origin(self):
        return f"{self.make} is from Japan"
    
    def __repr__(self):
        return f"make={self.make} model={self.model}"
    
    def __len__(self):
        return len(self.make) 
    

# object
car_one = Car("Toyota", "Hilux")

print(car_one)
print(len(car_one))