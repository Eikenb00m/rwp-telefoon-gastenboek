import RPi.GPIO as GPIO
import time

PWM_PIN = 18  # GPIO 18
MELODY = [
    (440, 0.5),  # A4 (440 Hz) voor 0.5 seconden
    (494, 0.5),  # B4 (494 Hz) voor 0.5 seconden
    (523, 0.5),  # C5 (523 Hz) voor 0.5 seconden
    (587, 1.0),  # D5 (587 Hz) voor 1.0 seconden
    (659, 1.0),  # E5 (659 Hz) voor 1.0 seconden
    (440, 1.5)   # Terug naar A4 voor 1.5 seconden
]

# GPIO configureren
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Start PWM
pwm = GPIO.PWM(PWM_PIN, 440)
pwm.start(50)  # 50% duty cycle

try:
    print("Speelt melodie...")
    for freq, duration in MELODY:
        print(f"Speelt {freq} Hz gedurende {duration} seconden.")
        pwm.ChangeFrequency(freq)
        time.sleep(duration)
    print("Melodie voltooid.")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO vrijgegeven.")
