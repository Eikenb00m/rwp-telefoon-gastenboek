import RPi.GPIO as GPIO
import time

PWM_PIN = 18  # GPIO 18
TONE_SEQUENCE = [
    (440, 0.5),  # 440 Hz voor 0.5 seconden
    (494, 0.5),  # 494 Hz voor 0.5 seconden
    (523, 0.5),  # 523 Hz voor 0.5 seconden
    (440, 1.0)   # 440 Hz voor 1.0 seconden
]

# GPIO configureren
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Start PWM
pwm = GPIO.PWM(PWM_PIN, 440)  # Standaard frequentie
pwm.start(50)  # 50% duty cycle

try:
    print("Speelt een reeks tonen...")
    for freq, duration in TONE_SEQUENCE:
        print(f"Speelt {freq} Hz gedurende {duration} seconden.")
        pwm.ChangeFrequency(freq)
        time.sleep(duration)
    print("Deuntje voltooid.")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO vrijgegeven.")
