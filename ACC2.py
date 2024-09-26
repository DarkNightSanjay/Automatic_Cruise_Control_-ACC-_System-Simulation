import time
import random

# Constants
MAX_SPEED = 80  # Maximum speed in km/h
SAFE_DISTANCE = 30  # Minimum safe distance in meters
SPEED_REDUCTION_RATE = 5  # Speed reduction rate in km/h when vehicle in front slows down

# Test Vehicle State
class TestVehicle:
    def __init__(self):
        self.speed = MAX_SPEED  # Current speed of the vehicle
        self.acc_active = False  # ACC status (on/off)
    
    def set_speed(self, speed):
        self.speed = speed
        print(f"Vehicle speed set to: {self.speed} km/h")
    
    def maintain_speed(self):
        print(f"Maintaining speed: {self.speed} km/h")

    def apply_brake(self, reduction):
        self.speed -= reduction
        self.speed = max(0, self.speed)  # Speed cannot go below 0
        print(f"Applying brake. Reducing speed by {reduction} km/h. Current speed: {self.speed} km/h")

    def resume_speed(self):
        if self.speed < MAX_SPEED:
            self.speed += SPEED_REDUCTION_RATE
            self.speed = min(self.speed, MAX_SPEED)  # Speed cannot exceed MAX_SPEED
            print(f"Resuming speed. Current speed: {self.speed} km/h")

# Front Vehicle Simulation (simulating behavior of the vehicle in front)
class FrontVehicle:
    def __init__(self):
        self.speed = MAX_SPEED  # Starts at 80 km/h

    def apply_brake(self):
        self.speed -= random.randint(5, 20)  # Random speed reduction
        self.speed = max(0, self.speed)
        print(f"Front vehicle is slowing down. Current speed: {self.speed} km/h")

    def change_lane(self):
        print("Front vehicle has changed lanes.")
        return True  # Simulating lane change

# Radar and Camera Simulation for detecting distance
def radar_detect_distance():
    return random.randint(10, 100)  # Random distance to simulate the radar data

def camera_detect_vehicle_in_lane():
    return random.choice([True, False])  # Randomly simulate vehicle presence in the same lane

# Main ACC Logic
def automatic_cruise_control(test_vehicle, front_vehicle):
    while True:
        distance = radar_detect_distance()
        print(f"Detected distance to front vehicle: {distance} meters")

        # Detect vehicle in the same lane using camera
        vehicle_in_lane = camera_detect_vehicle_in_lane()

        if vehicle_in_lane and distance <= SAFE_DISTANCE:
            # Front vehicle detected within unsafe distance
            test_vehicle.acc_active = True
            print("ACC is ON. Maintaining safe distance.")
            if front_vehicle.speed < test_vehicle.speed:
                # Apply brake if front vehicle slows down
                test_vehicle.apply_brake(SPEED_REDUCTION_RATE)
            else:
                test_vehicle.maintain_speed()
        elif not vehicle_in_lane:
            # No vehicle in front, turn off ACC and resume speed
            if test_vehicle.acc_active:
                test_vehicle.acc_active = False
                print("ACC is OFF. Resuming speed.")
            test_vehicle.resume_speed()
        else:
            # Maintain current speed if within safe distance and no speed difference
            test_vehicle.maintain_speed()

        # Simulate behavior of the front vehicle
        action = random.choice(['brake', 'change_lane', 'maintain'])
        if action == 'brake':
            front_vehicle.apply_brake()
        elif action == 'change_lane':
            if front_vehicle.change_lane():
                print("Front vehicle left the lane.")
        
        # Sleep to simulate time passage between checks
        time.sleep(2)

# Simulation
if __name__ == "__main__":
    test_vehicle = TestVehicle()
    front_vehicle = FrontVehicle()

    try:
        automatic_cruise_control(test_vehicle, front_vehicle)
    except KeyboardInterrupt:
        print("Simulation stopped.")
