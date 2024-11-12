import RPi.GPIO as GPIO
import time

PWM_PIN = 18  # GPIO 18
FREQ = 440  # Frequentie in Hz
DURATION = 5  # Duur in seconden

# GPIO configureren
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Start PWM met een duty cycle van 50% (vaste toon)
pwm = GPIO.PWM(PWM_PIN, FREQ)
pwm.start(50)  # 50% duty cycle

try:
    print(f"Speelt {FREQ} Hz toon gedurende {DURATION} seconden.")
    time.sleep(DURATION)
finally:
    pwm.stop()
    GPIO.cleanup()
    print("PWM gestopt en GPIO vrijgegeven.")
