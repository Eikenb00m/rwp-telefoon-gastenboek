import RPi.GPIO as GPIO
import wave
import numpy as np
import time

PWM_PIN = 18  # GPIO 18 voor PWM
WAV_FILE = "test.wav"  # Pad naar je WAV-bestand

# GPIO-instellingen
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

def play_wav(file_path):
    """Speel een WAV-bestand af via PWM."""
    with wave.open(file_path, "rb") as wav_file:
        sample_rate = wav_file.getframerate()
        num_channels = wav_file.getnchannels()

        if num_channels != 1:
            raise ValueError("Alleen mono-WAV-bestanden worden ondersteund.")

        print(f"Sample rate: {sample_rate} Hz")
        samples = np.frombuffer(wav_file.readframes(wav_file.getnframes()), dtype=np.int16)
        samples = (samples - np.min(samples)) / np.ptp(samples) * 100  # Normaliseer naar 0-100%

        pwm = GPIO.PWM(PWM_PIN, sample_rate)
        pwm.start(0)

        print("Afspelen gestart...")
        try:
            for sample in samples:
                pwm.ChangeDutyCycle(sample)
                time.sleep(1 / sample_rate)
        except KeyboardInterrupt:
            print("Afspelen onderbroken.")
        finally:
            pwm.stop()

try:
    play_wav(WAV_FILE)
finally:
    GPIO.cleanup()
    print("Afspelen voltooid.")
