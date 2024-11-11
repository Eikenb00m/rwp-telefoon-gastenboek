import RPi.GPIO as GPIO
import time
from pydub import AudioSegment
import numpy as np

# GPIO-configuratie
PWM_PIN = 18
FREQ = 44100  # Sample rate in Hz
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# MP3-bestand decoderen naar een numpy-array
def decode_mp3_to_pwm(mp3_file):
    print(f"Decodeer {mp3_file}...")
    audio = AudioSegment.from_file(mp3_file, format="mp3")  # Decodeer MP3
    samples = np.array(audio.get_array_of_samples())       # Converteer naar een numpy-array
    samples = samples / np.max(np.abs(samples))            # Normaliseer samples
    print("MP3 gedecodeerd.")
    return samples

# PWM-audio afspelen
def play_pwm(samples, duration):
    pwm = GPIO.PWM(PWM_PIN, FREQ)
    pwm.start(50)  # Start met een gemiddelde duty cycle
    print("Start PWM-audio...")

    try:
        for sample in samples:
            duty_cycle = (sample + 1) * 50  # Schaal naar 0-100%
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(1 / FREQ)
    except KeyboardInterrupt:
        print("Afspelen onderbroken.")
    finally:
        pwm.stop()
        GPIO.cleanup()
        print("PWM-audio gestopt.")

if __name__ == "__main__":
    MP3_FILE = "test.mp3"  # Vervang door je MP3-bestand
    samples = decode_mp3_to_pwm(MP3_FILE)
    play_pwm(samples, len(samples) / FREQ)
