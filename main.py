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
    print(f"Totaal aantal samples: {len(audio_samples)}")
    print("Start met afspelen...")
    for i, sample in enumerate(audio_samples):
        if i % 1000 == 0:  # Debug elk blok van 1000 samples
            print(f"Sample {i}: Duty cycle = {sample}%")
        pwm.ChangeDutyCycle(sample)  # Stel duty cycle in
        time.sleep(1 / SAMPLE_RATE)  # Houd de sample rate aan
    print("Afspelen voltooid.")
except Exception as e:
    print(f"Fout tijdens afspelen: {e}")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO vrijgegeven.")
