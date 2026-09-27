class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0 
        self.travelled_distance = 0 

    def accelerate(self, speed_change):
        self.current_speed = self.current_speed + speed_change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours_number):
        self.travelled_distance = self.travelled_distance + self.current_speed * hours_number 

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(150)
gasoline_car.accelerate(100)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric car: {electric_car.travelled_distance} km")
print(f"Gasoline car: {gasoline_car.travelled_distance} km")

