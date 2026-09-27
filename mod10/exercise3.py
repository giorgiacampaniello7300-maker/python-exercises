class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
    def floor_up(self):
        self.current += 1
        print(f"Elevator is at floor {self.current}")
    def floor_down(self):
        self.current -= 1
        print(f"Elevator is at floor {self.current}")
    def go_to_floor(self, floor):
        while self.current != floor:
            if self.current > floor:
                self.floor_down()
            else: 
                self.floor_up()

class Building:
    def __init__(self, bottom, top, elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for e in range(elevators):
            elevator = Elevator(bottom, top)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators: 
            elevator.go_to_floor(self.bottom)

building = Building(1, 10, 3)

building.run_elevator(1, 5)
building.run_elevator(2, 8)
building.fire_alarm()