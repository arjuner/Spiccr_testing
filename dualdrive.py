import time
import RPi.GPIO as GPIO

motor1_dir_pin = 24  # Direction control pin for Motor 1 (B1/B2)
motor1_enable_pin = 4  # Enable control pin for Motor 1
motor1_step_pin = 18  # Step control pin for Motor 1

motor2_dir_pin = 13  # Direction control pin for Motor 2 (A3/A4)
motor2_enable_pin = 12  # Enable control pin for Motor 2
motor2_step_pin = 19  # Step control pin for Motor 2

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(motor1_dir_pin, GPIO.OUT)
GPIO.setup(motor1_enable_pin, GPIO.OUT)
GPIO.setup(motor1_step_pin, GPIO.OUT)

GPIO.setup(motor2_dir_pin, GPIO.OUT)
GPIO.setup(motor2_enable_pin, GPIO.OUT)
GPIO.setup(motor2_step_pin, GPIO.OUT)

def run_motor(step_pin, dir_pin, enable_pin, duration):
    GPIO.output(enable_pin, GPIO.HIGH)  
    GPIO.output(dir_pin, GPIO.HIGH)  # Set direction forward
    
    # Run the motor for the specified duration
    print(f"Running motor for {duration} seconds...")
    start_time = time.time()
    while (time.time() - start_time) < duration:
        GPIO.output(step_pin, GPIO.HIGH)  # Step high
        time.sleep(0.01)  # Adjust delay for speed
        GPIO.output(step_pin, GPIO.LOW)  # Step low
        time.sleep(0.01)  # Adjust delay for speed
    
    GPIO.output(enable_pin, GPIO.LOW)  # Disable the motor

try:
    run_motor(motor1_step_pin, motor1_dir_pin, motor1_enable_pin, 5)
    
    # Change direction and run Motor 1 backward for 5 seconds
    GPIO.output(motor1_dir_pin, GPIO.LOW)  # Set direction backward
    run_motor(motor1_step_pin, motor1_dir_pin, motor1_enable_pin, 5)

    run_motor(motor2_step_pin, motor2_dir_pin, motor2_enable_pin, 5)

    # Change direction and run Motor 2 backward for 5 seconds
    GPIO.output(motor2_dir_pin, GPIO.LOW)  # Set direction backward
    run_motor(motor2_step_pin, motor2_dir_pin, motor2_enable_pin, 5)

finally:
    GPIO.cleanup()  
    print("GPIO cleanup done.")
