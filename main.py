import RPi.GPIO as GPIO
import time

PWM_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

pwm = GPIO.PWM(PWM_PIN, 440)  # 440 Hz toon
pwm.start(50)  # 50% duty cycle

print("Speelt een toon van 440 Hz. Stop na 5 seconden.")
time.sleep(5)

pwm.stop()
GPIO.cleanup()
