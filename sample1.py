class vehicle:
    def __init__(self):
        print("i am used for transportation")

    def bus(self):
        self.wheels=6
        print("i am in bus")
class car(vehicle):
    def __init__(self):
        self.wheels=4
        print("i am in car")


class cycle(car):
    def __init__(self):
          print("i am on cycle")
class scate(cycle):
    def __init__(self):
        print("i am wearing scates")


self=b=scate()
cycle.__init__(self)

print(issubclass(vehicle,car))

