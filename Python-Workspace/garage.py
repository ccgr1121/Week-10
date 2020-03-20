from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, engine_size):
        self.engine_size=engine_size
    
    @abstractmethod
    def movement(self):
        pass

class Car(Vehicle):
    def __init__(self, reg_plate, engine_size):
        super().__init__(engine_size)
        self.reg_plate = reg_plate
    
    def movement(self):
        return "brum brum"