#This code is for JGY-370 Dc motors for 600 Spiccr

import machine
import time

# Define motor control pins
IN1 = machine.Pin(2, machine.Pin.OUT)  # Motor A Direction
IN2 = machine.Pin(3, machine.Pin.OUT)  # Motor A Direction
IN3 = machine.Pin(4, machine.Pin.OUT)  # Motor B Direction
IN4 = machine.Pin(5, machine.Pin.OUT)  # Motor B Direction

# Function to control motors
def motor_control(motor, direction):
    if motor == "A":
        if direction == "forward":
            IN1.value(1)
            IN2.value(0)
        elif direction == "backward":
            IN1.value(0)
            IN2.value(1)
        else:
            IN1.value(0)
            IN2.value(0)  # Stop
    elif motor == "B":
        if direction == "forward":
            IN3.value(1)
            IN4.value(0)
        elif direction == "backward":
            IN3.value(0)
            IN4.value(1)
        else:
            IN3.value(0)
            IN4.value(0)  # Stop

# Main program
try:
    print("Running motors forward for 8 seconds")
    motor_control("A", "forward")  # Motor A forward
    motor_control("B", "forward")  # Motor B forward
    time.sleep(8)

    print("Running motors backward for 8 seconds")
    motor_control("A", "backward")  # Motor A backward
    motor_control("B", "backward")  # Motor B backward
    time.sleep(8)

    print("Stopping motors")
    motor_control("A", "stop")  # Stop Motor A
    motor_control("B", "stop")  # Stop Motor B

except KeyboardInterrupt:
    print("Program interrupted. Stopping motors.")
    motor_control("A", "stop")
    motor_control("B", "stop")

