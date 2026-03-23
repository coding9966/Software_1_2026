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


# --- Main program: Car race ---
if __name__ == "__main__":
    # Create a list of 10 cars
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)  # Random max speed between 100 and 200 km/h
        reg_number = f"ABC-{i}"
        cars.append(Car(reg_number, max_speed))

    # Race until one car reaches at least 10,000 km
    race_over = False
    hour = 0
    while not race_over:
        hour += 1
        for car in cars:
            # Random speed change between -10 and +15 km/h
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            # Drive for 1 hour at current speed
            car.drive(1)
            # Check if any car reached 10,000 km
            if car.travelled_distance >= 10000:
                race_over = True

    # Print final results in a table
    print("\nFinal results after the race:")
    print(f"{'Reg. Number':<12} {'Max Speed':<10} {'Current Speed':<15} {'Travelled Distance':<20}")
    print("-" * 60)
    for car in cars:
        print(f"{car.registration_number:<12} {car.max_speed:<10} {car.current_speed:<15} {car.travelled_distance:<20.1f}")