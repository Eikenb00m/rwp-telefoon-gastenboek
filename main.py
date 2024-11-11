import RPi.GPIO as GPIO
import time

PWM_PIN = 18  # GPIO 18 (BCM-modus)

# GPIO-instellingen
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Start PWM op GPIO 18
pwm = GPIO.PWM(PWM_PIN, 100)  # 100 Hz
pwm.start(0)  # Start met 0% duty cycle

try:
    while True:
        for duty_cycle in range(0, 101, 5):  # Verhoog helderheid
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)
        for duty_cycle in range(100, -1, -5):  # Verlaag helderheid
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)
except KeyboardInterrupt:
    print("PWM-test gestopt.")
finally:
    pwm.stop()
    GPIO.cleanup()
