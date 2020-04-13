class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def openAirConditioner(self):
        print("Turn on : Air")
class Car(Vehicle):
    def Type(self):
        print("This is car")

class Van(Vehicle):
    def Type(self):
        print("This is van")

class PickUp(Vehicle):
    def Type(self):
        print("This is pick up")

car1 = Car()
car1.openAirConditioner()
car1.Type()
print("---------")
van1 = Van()
van1.openAirConditioner()
van1.Type()
print("---------")
pickUp1 = PickUp()
pickUp1.openAirConditioner()
pickUp1.Type()

