class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        """Change the car's speed by the given amount, respecting limits."""
        self.current_speed += change
        # Ensure speed stays within 0 and max_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        print(f"Current speed: {self.current_speed} km/h")


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
    my_car.accelerate(50)  # Should cap at 142 km/h

    # Print current speed
    print(f"\nCurrent speed after accelerations: {my_car.current_speed} km/h")

    # Emergency brake
    print("\nEmergency brake (-200 km/h):")
    my_car.accelerate(-200)  # Should set speed to 0

    # Print final speed
    print(f"Final speed: {my_car.current_speed} km/h")