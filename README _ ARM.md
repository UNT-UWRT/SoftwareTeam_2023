#ARM NOTES

Spin each motor clockwise and counter-clockwise at speeds and angles specified by the controller.
Two of the motors (base and rotational) has speed and angle controls, while one motor (claw motor) has revolution controls (i.e. do 5 revolutions).
The gear ratio for the motors is 20:1.
Using the RT and LT triggers on an Xbox controller to control the claw rotation and the RB and LB buttons to open and close the claw.


The code sets up the GPIO pins for the three motors and defines constants for motor control. 
The move_motor() function is used to move a motor a certain number of steps in a specified direction.

The code then enters a loop to read inputs from the Xbox controller. 
If a trigger button is pressed, the code sets the motor direction based on the button pressed and calculates the number of steps to move the motor based on the trigger position. 
It then moves the motor the specified number of steps in the specified direction.

If a bumper button is pressed, the code determines which motor to control based on the button pressed and moves the motor a fixed number of steps to open or close the claw.

***This is still a work in progress. I have no idea if this code would work.
