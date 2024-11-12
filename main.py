import RPi.GPIO as GPIO
import time
import numpy as np

PWM_PIN = 18
FREQ = 440  # Frequentie in Hz (A4)
DURATION = 5  # Duur in seconden
SAMPLE_RATE = 48000  # Sample rate in Hz

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Sinusgolf genereren
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
sin_wave = 50 + 50 * np.sin(2 * np.pi * FREQ * t)  # Duty cycle tussen 0-100%

pwm = GPIO.PWM(PWM_PIN, SAMPLE_RATE)
pwm.start(0)

try:
    print(f"Speelt {FREQ} Hz toon gedurende {DURATION} seconden.")
    for sample in sin_wave:
        pwm.ChangeDutyCycle(sample)
        time.sleep(1 / SAMPLE_RATE)
finally:
    pwm.stop()
    GPIO.cleanup()
    print("PWM gestopt en GPIO vrijgegeven.")
