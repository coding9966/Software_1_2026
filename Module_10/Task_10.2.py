class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor  # Elevator starts at bottom

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Floor up! Current floor: {self.current_floor}")
        else:
            print("Already at the top floor!")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Floor down! Current floor: {self.current_floor}")
        else:
            print("Already at the bottom floor!")

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print("Floor out of range!")
            return
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()
        if self.current_floor == floor:
            print(f"Arrived at floor {self.current_floor}!")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print("Invalid elevator number!")
            return
        print(f"\nRunning Elevator {elevator_number} to floor {destination_floor}")
        self.elevators[elevator_number - 1].go_to_floor(destination_floor)


# --- Testing the Building and Elevator classes ---
if __name__ == "__main__":
    # Create a building with floors 1-10 and 3 elevators
    my_building = Building(1, 10, 3)

    # Run elevators
    my_building.run_elevator(1, 5)   # Elevator 1 to floor 5
    my_building.run_elevator(2, 8)   # Elevator 2 to floor 8
    my_building.run_elevator(3, 1)   # Elevator 3 to floor 1 (already at bottom)