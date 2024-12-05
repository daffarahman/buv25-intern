# Car Polymorphism

class Car:
    def __init__(self, name, top_speed, price):
        self.name = name
        self.top_speed = top_speed
        self.price = price

    def drive(self, speed):
        if speed > self.top_speed:
            print(f"{self.name}'s top speed reached!!!")
        elif speed <= self.top_speed and speed > 0:
            print(f"{self.name} vrooom vroooom {speed}kmh!!! ......")
        elif speed == 0:
            print(f"{self.name} stopped!")
        else:    
            print(f"{self.name} going backwards!")

    def __str__(self):
        return str(self.name)


class PoliceCar(Car):
    def __init__(self, top_speed):
        super().__init__("Police", top_speed, 1000)
    
    def catch(self, car):
        if self.top_speed >= car.top_speed:
            print(f"Catched {car.name}!!")
        else:
            print(f"Can't catch {car.name}... it's 2 fast and 2 furious!!")


supra = Car("Supra", 300, 100000)
r34 = Car("Skyline R34", 250, 80000)
silverado = Car("Chevy Silverado", 150, 35000)

police = PoliceCar(200)

police.catch(supra)
police.catch(silverado)
