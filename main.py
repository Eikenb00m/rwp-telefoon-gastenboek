import RPi.GPIO as GPIO
import time

PWM_PIN = 18  # GPIO 18
FREQ = 440    # Toonfrequentie (Hz)
DURATION = 5  # Duur in seconden

# GPIO-configuratie
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Start PWM
pwm = GPIO.PWM(PWM_PIN, FREQ)
pwm.start(50)  # 50% duty cycle

print(f"Speel een {FREQ} Hz toon gedurende {DURATION} seconden.")
time.sleep(DURATION)

# Stop PWM
pwm.stop()
GPIO.cleanup()
print("PWM gestopt.")
