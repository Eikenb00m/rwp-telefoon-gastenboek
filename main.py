import RPi.GPIO as GPIO
import time
import wave
import numpy as np
from scipy.signal import resample

# Configuratie
PWM_PIN = 18  # GPIO 18 voor PWM
TARGET_SAMPLE_RATE = 44100  # Doelsample rate
WAV_FILE = "test.wav"  # Pad naar je WAV-bestand

# GPIO-instellingen
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

def stereo_to_mono(frames, num_channels):
    """Converteer stereo-audio naar mono door gemiddeldes te nemen."""
    samples = np.frombuffer(frames, dtype=np.int16)
    if num_channels == 2:  # Als het stereo is
        samples = samples.reshape(-1, 2)  # Split stereo naar twee kanalen
        samples = samples.mean(axis=1).astype(np.int16)  # Gemiddelde van beide kanalen
    return samples

def resample_audio(samples, original_rate, target_rate):
    """Herschalen van audio naar de doelsample rate."""
    if original_rate == target_rate:
        return samples  # Geen aanpassing nodig
    print(f"Herschaal audio van {original_rate} Hz naar {target_rate} Hz...")
    num_samples = int(len(samples) * target_rate / original_rate)
    resampled = resample(samples, num_samples)
    return resampled.astype(np.float32)

def play_wav(file_path):
    """Speel een WAV-bestand af via PWM."""
    with wave.open(file_path, "rb") as wav_file:
        # Haal audio-informatie op
        num_channels = wav_file.getnchannels()
        original_rate = wav_file.getframerate()

        # Lees frames en converteer naar numpy-array
        frames = wav_file.readframes(wav_file.getnframes())
        samples = stereo_to_mono(frames, num_channels)  # Converteer naar mono als nodig

        # Herschalen naar 44100 Hz
        samples = resample_audio(samples, original_rate, TARGET_SAMPLE_RATE)

        # Normaliseer samples naar -1 tot 1
        samples = samples / np.max(np.abs(samples))

        # Start PWM
        pwm = GPIO.PWM(PWM_PIN, TARGET_SAMPLE_RATE)  # PWM met doelsample rate
        pwm.start(50)  # Start met een gemiddelde duty cycle

        print(f"Speelt {file_path} af...")
        try:
            for sample in samples:
                # Converteer sample naar duty cycle (0-100%)
                duty_cycle = (sample + 1) * 50
                pwm.ChangeDutyCycle(duty_cycle)
                time.sleep(1 / TARGET_SAMPLE_RATE)
        except KeyboardInterrupt:
            print("Afspelen onderbroken.")
        finally:
            pwm.stop()

# Start afspelen
try:
    play_wav(WAV_FILE)
finally:
    GPIO.cleanup()
    print("Afspelen voltooid.")
