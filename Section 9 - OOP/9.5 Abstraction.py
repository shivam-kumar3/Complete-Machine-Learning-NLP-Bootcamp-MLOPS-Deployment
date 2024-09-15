'''
ABSTRATION 

ABSTRACTION IS THE CONCEPT OF HIDING THE COMPLEX IMPLEMENTATION DETAILS AND SHOWING ONLY THE NECESSARY FEATURES OF AN OBJECT. THIS HELPS IN REDUCING PROGRAMMING COMPLEXITY AND EFFORTS

'''

from abc import ABC , abstractmethod

# abstract base class
class Vehicle(ABC):
    def drive(self):
        print("The vehicle for used for driving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

def operate_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.drive()

car = Car()
operate_vehicle(car)