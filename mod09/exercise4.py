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

cars = []

for c in range(1, 11):
    registration_number = "ABC-" + str(c)
    maximum_speed = random.randint(100, 200)
    car = Car(registration_number, maximum_speed)
    cars.append(car)


race_finished = False

while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True


print("Registration   Maximum speed   Current speed   Travelled distance")

for car in cars:
    print(f"{car.registration_number}          {car.maximum_speed} km/h         {car.current_speed} km/h         {car.travelled_distance} km")