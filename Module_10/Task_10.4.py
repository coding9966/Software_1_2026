import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        """Change the car's speed by the given amount, keeping speed within 0 and max_speed."""
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        """Increase travelled distance based on current speed and given time in hours."""
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        """Perform one hour of the race: random speed changes and drive for 1 hour."""
        for car in self.cars:
            speed_change = random.randint(-10, 15)  # Random speed change
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        """Print the current status of each car in a formatted table."""
        print(f"\n{'Reg. Number':<12} {'Max Speed':<10} {'Current Speed':<15} {'Travelled Distance':<20}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.registration_number:<12} {car.max_speed:<10} {car.current_speed:<15} {car.travelled_distance:<20.1f}")

    def race_finished(self):
        """Return True if any car has reached or exceeded the race distance."""
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False


# --- Main program ---
if __name__ == "__main__":
    # Create 10 cars
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        reg_number = f"ABC-{i}"
        cars.append(Car(reg_number, max_speed))

    # Create a race of 8000 km
    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    # Simulate the race
    while not race.race_finished():
        hours += 1
        race.hour_passes()

        # Print status every 10 hours
        if hours % 10 == 0:
            print(f"\n--- Status after {hours} hours ---")
            race.print_status()

    # Print final race status
    print(f"\n--- Final status after {hours} hours ---")
    race.print_status()