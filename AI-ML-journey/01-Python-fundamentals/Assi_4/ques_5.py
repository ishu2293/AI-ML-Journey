class vehicle:
    brand = "mercedes"
    model = 12

class car(vehicle):
    def __init__(self, seats):
        self.seats = seats

    def showC(self):
        print(f"Car with brand {self.brand} and model {self.model} has seats {self.seats}")

class bike(vehicle):
    def __init__(self, engine):
        self.engine = engine

    def showB(self):
        print(f"Car with brand {self.brand} and model {self.model} has engine_cc {self.engine}")        

# car1 = car(4)
# car1.showC()        

bike1 = bike(400)
bike1.showB()