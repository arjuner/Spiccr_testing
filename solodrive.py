import time
import RPi.GPIO as GPIO

    # Define GPIO pins for controlling the motor via the HAT
dir_pin = 13  # Direction control pin (A1/A2)
enable_pin = 12  # Enable control pin
step_pin = 19  # Enable control pin


    # Setup GPIO
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)



try:
        # Enable the motor
    GPIO.output(enable_pin, GPIO.HIGH)  # Enable the motor

        # Run motor forward for 10 seconds
    print("Motor running forward for 10 seconds...")
    GPIO.output(dir_pin, GPIO.HIGH)  # Set direction forward
    GPIO.output(step_pin, GPIO.HIGH)  # Set direction forward
    time.sleep(5)                    # Run for 10 seconds

        # Stop the motor
    print("Motor stopping...")
    GPIO.output(enable_pin, GPIO.LOW)  # Disable the motor
    time.sleep(1)                      # Wait for 1 second

        # Enable the motor again
    GPIO.output(enable_pin, GPIO.HIGH)  # Enable the motor

        # Run motor backward for 10 seconds
    print("Motor running backward for 10 seconds...")
    GPIO.output(dir_pin, GPIO.LOW)   # Set direction backward
    GPIO.output(step_pin, GPIO.LOW)  # Set direction forward

    time.sleep(5)                   # Run for 10 seconds

        # Stop the motor
    print("Motor stopping...")
    GPIO.output(enable_pin, GPIO.LOW)  # Disable the motor

finally:
    GPIO.cleanup()  # Clean up GPIO pins
    print("GPIO cleanup done.")

