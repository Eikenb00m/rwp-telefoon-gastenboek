import RPi.GPIO as GPIO
import wave
import numpy as np
import time

# GPIO-configuratie
PWM_PIN = 18  # GPIO 18 voor PWM
WAV_FILE = "test.wav"  # Pad naar je WAV-bestand

# GPIO-instellingen
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

def play_wav(file_path):
    """Speel een WAV-bestand af via PWM."""
    with wave.open(file_path, "rb") as wav_file:
        # Controleer WAV-parameters
        sample_rate = wav_file.getframerate()
        num_channels = wav_file.getnchannels()
        num_frames = wav_file.getnframes()

        print(f"Sample rate: {sample_rate} Hz, Kanalen: {num_channels}, Frames: {num_frames}")

        if num_channels != 1:
            raise ValueError("Alleen mono WAV-bestanden worden ondersteund.")

        # Lees audiosamples
        frames = wav_file.readframes(num_frames)
        samples = np.frombuffer(frames, dtype=np.int16)

        # Normaliseer samples naar een bereik van 0-100%
        samples = ((samples - np.min(samples)) / np.ptp(samples) * 100).astype(np.uint8)

        # Start PWM
        pwm = GPIO.PWM(PWM_PIN, sample_rate)
        pwm.start(0)  # Start met duty cycle 0%

        print("Afspelen gestart...")
        try:
            for i, sample in enumerate(samples):
                if i % 1000 == 0:  # Debug elke 1000 samples
                    print(f"Sample {i}: Duty cycle = {sample}%")
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
