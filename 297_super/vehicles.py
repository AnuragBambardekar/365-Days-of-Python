class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"Starting the engine of {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def start_engine(self):
        super().start_engine()  # Call the start_engine method of the parent class
        print(f"Fuel type: {self.fuel_type}")

class Bicycle(Vehicle):
    def __init__(self, brand, model, frame_material):
        super().__init__(brand, model)
        self.frame_material = frame_material

    def start_engine(self):
        print(f"This is a bicycle. No engine to start.")
        print(f"Frame material: {self.frame_material}")

# Creating instances of the classes
car = Car("Toyota", "Camry", "Gasoline")
bicycle = Bicycle("Trek", "Mountain Bike", "Aluminum")

# Calling start_engine method for both instances
car.start_engine()
print("\n")
bicycle.start_engine()
