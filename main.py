import RPi.GPIO as GPIO
import time
from audio_samples import audio_samples

PWM_PIN = 18
SAMPLE_RATE = 48000

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)
pwm = GPIO.PWM(PWM_PIN, SAMPLE_RATE)
pwm.start(0)

try:
    print("Speelt audiofragment af...")
    for i in range(0, len(audio_samples), 100):  # Speel blokken van 100 samples
        for sample in audio_samples[i:i+100]:
            pwm.ChangeDutyCycle(sample)
        time.sleep(100 / SAMPLE_RATE)  # Wacht de tijd voor 100 samples
    print("Afspelen voltooid.")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO vrijgegeven.")
