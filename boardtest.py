import RPi.GPIO as GPIO
import time


# Suppress GPIO warnings
GPIO.setwarnings(False)

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)  # Use BCM numbering

# TB6612FNG Motor Driver 1 Pins (BCM)
PWM_A1 = 19  # GPIO 19
AIN1_1 = 6   # GPIO 5
AIN2_1 = 5   # GPIO 6
PWM_B1 = 13  # GPIO 13
BIN1_1 = 26  # GPIO 26
BIN2_1 = 16  # GPIO 16

# TB6612FNG Motor Driver 2 Pins (BCM)
PWM_A2 = 18  # GPIO 18
AIN1_2 = 23  # GPIO 23
AIN2_2 = 24  # GPIO 24
PWM_B2 = 12  # GPIO 12
BIN1_2 = 25  # GPIO 25
BIN2_2 = 22  # GPIO 22

# Setup the pins for all motors
pins_motor1 = [PWM_A1, AIN1_1, AIN2_1, PWM_B1, BIN1_1, BIN2_1]
pins_motor2 = [PWM_A2, AIN1_2, AIN2_2, PWM_B2, BIN1_2, BIN2_2]

# Cleanup any previous setup
GPIO.cleanup()

for pin in pins_motor1 + pins_motor2:
    GPIO.setup(pin, GPIO.OUT)

# Setup PWM for both motors
pwm_a1 = GPIO.PWM(PWM_A1, 1000)  # PWM on Motor A1 at 1kHz
pwm_b1 = GPIO.PWM(PWM_B1, 1000)  # PWM on Motor B1 at 1kHz
pwm_a2 = GPIO.PWM(PWM_A2, 1000)  # PWM on Motor A2 at 1kHz
pwm_b2 = GPIO.PWM(PWM_B2, 1000)  # PWM on Motor B2 at 1kHz

# Start PWM with 0% duty cycle (off)
pwm_a1.start(0)
pwm_b1.start(0)
pwm_a2.start(0)
pwm_b2.start(0)

# Function to control all motors with PWM
def control_all_motors(direction, speed):
    if direction == 'forward':
        GPIO.output(AIN1_1, GPIO.HIGH)
        GPIO.output(AIN2_1, GPIO.LOW)
        GPIO.output(BIN1_1, GPIO.HIGH)
        GPIO.output(BIN2_1, GPIO.LOW)

        GPIO.output(AIN1_2, GPIO.HIGH)
        GPIO.output(AIN2_2, GPIO.LOW)
        GPIO.output(BIN1_2, GPIO.HIGH)
        GPIO.output(BIN2_2, GPIO.LOW)

    elif direction == 'backward':
        GPIO.output(AIN1_1, GPIO.LOW)
        GPIO.output(AIN2_1, GPIO.HIGH)
        GPIO.output(BIN1_1, GPIO.LOW)
        GPIO.output(BIN2_1, GPIO.HIGH)

        GPIO.output(AIN1_2, GPIO.LOW)
        GPIO.output(AIN2_2, GPIO.HIGH)
        GPIO.output(BIN1_2, GPIO.LOW)
        GPIO.output(BIN2_2, GPIO.HIGH)

    # Set the speed (duty cycle)
    pwm_a1.ChangeDutyCycle(speed)
    pwm_b1.ChangeDutyCycle(speed)
    pwm_a2.ChangeDutyCycle(speed)
    pwm_b2.ChangeDutyCycle(speed)

# Test All Motors with PWM Speed Control
try:
    # Run all motors Forward at 75% speed
    print("Running all motors Forward at 75% speed")
    control_all_motors('forward', 100)
    time.sleep(5)  # Run for 2 seconds

    # Run all motors Backward at 50% speed
    print("Running all motors Backward at 50% speed")
    control_all_motors('backward', 100)
    time.sleep(5)  # Run for 2 seconds

finally:
    # Stop all motors and cleanup
    pwm_a1.stop()
    pwm_b1.stop()
    pwm_a2.stop()
    pwm_b2.stop()
    
    for pin in pins_motor1 + pins_motor2:
        GPIO.output(pin, GPIO.LOW)  # Turn off all motors

    GPIO.cleanup()  # Cleanup GPIO sett
