class Engine:
    def __init__(self, volume, horse_power):
        self.volume = volume
        self.horse_power = horse_power

    def start(self):
        return "Vroooooom"

    def stop(self):
        return "stopped"


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def drive(self):
        return self.engine.start()
    
engine1 = Engine(6, 100)
print(engine1.volume)
print(engine1.start())

car1 = Car("Opel", "Manta", engine1)
print(car1.make)
print(car1.drive)