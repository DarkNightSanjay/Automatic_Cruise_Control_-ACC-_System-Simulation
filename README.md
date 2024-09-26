# Automatic Cruise Control (ACC) System Simulation

This repository contains a Python-based simulation of an Automatic Cruise Control (ACC) system. The system is designed to simulate the behavior of a test vehicle equipped with ACC, as well as the vehicle in front of it, along with radar and camera sensors. The ACC system dynamically adjusts the speed of the test vehicle to maintain a safe distance from the vehicle in front.

## Features

- **Speed Control:** The test vehicle's speed is automatically adjusted based on the distance to the vehicle in front.
- **Radar Simulation:** A simulated radar detects the distance between the test vehicle and the vehicle in front.
- **Camera Simulation:** A simulated camera determines if the vehicle in front is in the same lane.
- **Braking and Speed Resumption:** The test vehicle applies brakes if the front vehicle slows down and resumes speed when the road is clear.
- **Front Vehicle Behavior:** The front vehicle's speed changes randomly, simulating real-world driving conditions.

## How It Works

1. The test vehicle starts at a constant speed of 80 km/h (which can be adjusted).
2. A simulated radar detects the distance to the vehicle in front, while the simulated camera checks if the front vehicle is in the same lane.
3. If the front vehicle slows down and is within an unsafe distance (less than 30 meters), the test vehicle automatically applies brakes to maintain a safe following distance.
4. Once the front vehicle changes lanes or moves away, the test vehicle resumes its speed up to the maximum allowed speed.

## Constants

- **MAX_SPEED:** The maximum speed of the test vehicle (default: 80 km/h).
- **SAFE_DISTANCE:** The safe distance threshold that the ACC system maintains from the vehicle in front (default: 30 meters).
- **SPEED_REDUCTION_RATE:** The rate at which the vehicle decelerates when the front vehicle slows down (default: 5 km/h).

## Usage

1. Clone this repository:

       git clone https://github.com/your-username/acc-system-simulation.git
       cd acc-system-simulation

### Run the simulation:
    python acc_simulation.py
The simulation will run continuously until manually stopped (e.g., using Ctrl+C).

### Simulation Output
The simulation will output information about:
- Detected distance to the front vehicle.
- Whether the front vehicle is in the same lane.
- The current speed of both the test and front vehicles.
- Actions taken by the ACC system (such as braking or resuming speed).
### Requirements
    Python 3.x
### Example Output
    Detected distance to front vehicle: 25 meters
    ACC is ON. Maintaining safe distance.
    Applying brake. Reducing speed by 5 km/h. Current speed: 75 km/h
    Front vehicle is slowing down. Current speed: 60 km/h
    Detected distance to front vehicle: 60 meters
    ACC is OFF. Resuming speed.
    Resuming speed. Current speed: 80 km/h
    Front vehicle has changed lanes.
    Front vehicle left the lane.
### Future Improvements
- Incorporating more realistic vehicle dynamics.
- Improving sensor accuracy and detection behavior.
- Adding more complex driving scenarios (e.g., highway merging, lane changes, multiple vehicles).
- GUI integration for better visualization of the ACC system.
