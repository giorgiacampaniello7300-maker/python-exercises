import random 

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

class Race:
    def __init__(self, name, kilometers, cars):
        self.name = name
        self.kilometers = kilometers
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print("Registration  Maximum speed  Current speed  Travelled distance")
        for car in self.cars:
            print(f"{car.registration_number}         {car.maximum_speed} km/h        {car.current_speed} km/h        {car.travelled_distance} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.kilometers:
                return True
        return False

cars = []

for c in range(1, 11):
    registration_number = "ABC-" + str(c)
    maximum_speed = random.randint(100, 200)
    car = Car(registration_number, maximum_speed)
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)
hours = 0

while not race.race_finished():
    race.hour_passes()
    hours = hours + 1

    if hours % 10 == 0:
        race.print_status()

race.print_status()