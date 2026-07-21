class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self , name): 
        self.name = name

c1 = ToyotaCar("fortuner")
c2 = ToyotaCar("Lengendar")

print(c1.name)
c1.stop()
