import RPi.GPIO as GPIO
from time import sleep
from inputs import get_gamepad

# Set up GPIO pins for the three stepper motors
base_motor_pins = [4, 17, 27, 22]
rotational_motor_pins = [6, 13, 19, 26]
claw_motor_pins = [5, 12, 16, 20]

for pins in [base_motor_pins, rotational_motor_pins, claw_motor_pins]:
    GPIO.setup(pins, GPIO.OUT)
    GPIO.output(pins, 0)

# Define some constants for the motor control
STEP_DELAY = 0.001  # Delay between each step
STEPS_PER_REVOLUTION = 200  # Number of steps per motor revolution
GEAR_RATIO = 20  # Gear ratio of the motors

# Function to move a motor a certain number of steps
def move_motor(pins, steps):
    for i in range(steps):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(pins[pin], halfstep & (1 << pin))
            sleep(STEP_DELAY)

# Loop to read inputs from the Xbox controller and control the motors
while True:
    events = get_gamepad()
    for event in events:
        # Check if the event is a trigger button press or release
        if event.ev_type == 'Key' and event.code in ['BTN_TL', 'BTN_TR']:
            # Set the motor direction based on the button that was pressed
            if event.code == 'BTN_TL':
                direction = -1  # Counterclockwise
            else:
                direction = 1  # Clockwise
            
            # Determine which motor to control based on the button that was pressed
            if event.ev_type == 'Key' and event.code == 'BTN_TL':
                pins = claw_motor_pins
            else:
                pins = rotational_motor_pins
            
            # Calculate the number of steps to move the motor based on the trigger position
            steps = int(abs(event.state * GEAR_RATIO * STEPS_PER_REVOLUTION * 2 * 3.14 / 360))
            
            # Move the motor the specified number of steps in the specified direction
            move_motor(pins, direction * steps)
            
        # Check if the event is a bumper button press
        elif event.ev_type == 'Key' and event.code in ['BTN_TL2', 'BTN_TR2']:
            # Determine which motor to control based on the button that was pressed
            if event.ev_type == 'Key' and event.code == 'BTN_TL2':
                pins = claw_motor_pins
            else:
                pins = base_motor_pins
            
            # Move the motor a fixed number of steps to open or close the claw
            if event.state:
                move_motor(pins, 100)  # Close the claw
            else:
                move_motor(pins, -100)  # Open the claw
