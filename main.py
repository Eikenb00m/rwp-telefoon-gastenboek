import RPi.GPIO as GPIO
import time
import random

PWM_PIN = 18  # GPIO 18

# GPIO configureren
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Start PWM
pwm = GPIO.PWM(PWM_PIN, 440)
pwm.start(50)

try:
    print("Speelt willekeurige tonen...")
    for _ in range(10):  # Speel 10 willekeurige tonen
        freq = random.randint(300, 1000)  # Willekeurige frequentie tussen 300 en 1000 Hz
        duration = random.uniform(0.2, 1.0)  # Willekeurige duur tussen 0.2 en 1.0 seconden
        print(f"Speelt {freq} Hz gedurende {duration:.2f} seconden.")
        pwm.ChangeFrequency(freq)
        time.sleep(duration)
    print("Random tonen voltooid.")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO vrijgegeven.")
