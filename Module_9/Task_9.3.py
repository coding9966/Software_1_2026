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
        print(f"Current speed: {self.current_speed} km/h")

    def drive(self, hours):
        """Increase travelled distance based on current speed and given time in hours."""
        distance = self.current_speed * hours
        self.travelled_distance += distance
        print(f"Travelled distance: {self.travelled_distance:.1f} km")


# --- Main program ---
if __name__ == "__main__":
    # Create a new car
    my_car = Car("ABC-123", 142)

    # Accelerate in steps
    print("Accelerating +30 km/h:")
    my_car.accelerate(30)

    print("Accelerating +70 km/h:")
    my_car.accelerate(70)

    print("Accelerating +50 km/h:")
    my_car.accelerate(50)  # Speed caps at 142 km/h

    # Print current speed
    print(f"\nCurrent speed after accelerations: {my_car.current_speed} km/h")

    # Drive for 1.5 hours
    print("\nDriving for 1.5 hours at current speed:")
    my_car.drive(1.5)  # Travelled distance increases by 142 * 1.5 = 213 km

    # Emergency brake
    print("\nEmergency brake (-200 km/h):")
    my_car.accelerate(-200)  # Speed set to 0

    # Drive for 2 hours at 0 km/h
    print("\nDriving for 2 hours at current speed (0 km/h):")
    my_car.drive(2)  # Travelled distance stays the same

    # Print final travelled distance
    print(f"\nFinal travelled distance: {my_car.travelled_distance:.1f} km")