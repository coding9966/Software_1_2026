class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor  # Elevator always starts at bottom

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

if __name__ == "__main__":
    h = Elevator(1, 10)  # Bottom floor 1, top floor 10
    print(f"Elevator starting at floor {h.current_floor}")

    h.go_to_floor(5)  # Move to floor 5
    h.go_to_floor(1)  # Move back to bottom floor