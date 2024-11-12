import RPi.GPIO as GPIO
import time
from audio_samples import audio_samples  # Importeer de gegenereerde audio array

PWM_PIN = 18  # GPIO 18
SAMPLE_RATE = 48000  # Sample rate van de audio

# GPIO-configuratie
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Start PWM op de juiste sample rate
pwm = GPIO.PWM(PWM_PIN, SAMPLE_RATE)
pwm.start(0)  # Begin met een duty cycle van 0%

try:
    print("Speelt audiofragment af...")
    for sample in audio_samples:
        pwm.ChangeDutyCycle(sample)  # Stel duty cycle in op basis van de sample
        time.sleep(1 / SAMPLE_RATE)  # Wacht tot de volgende sample
    print("Afspelen voltooid.")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO vrijgegeven.")
