import RPi.GPIO as GPIO
import time
import wave
import numpy as np

# Configuratie
PWM_PIN = 18  # GPIO 18 voor PWM
SAMPLE_RATE = 44100  # Verwachte sample rate (in Hz)
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

def play_wav(file_path):
    """Speel een WAV-bestand af via PWM."""
    with wave.open(file_path, "rb") as wav_file:
        # Haal audio-informatie op
        num_channels = wav_file.getnchannels()
        framerate = wav_file.getframerate()

        if framerate != SAMPLE_RATE:
            raise ValueError(f"Sample rate moet {SAMPLE_RATE} Hz zijn, gevonden {framerate} Hz.")

        # Lees frames en converteer naar numpy-array
        frames = wav_file.readframes(wav_file.getnframes())
        samples = stereo_to_mono(frames, num_channels)  # Converteer naar mono als nodig
        samples = samples / np.max(np.abs(samples))  # Normaliseer samples naar -1 tot 1

        # Start PWM
        pwm = GPIO.PWM(PWM_PIN, SAMPLE_RATE)  # PWM met de sample rate als frequentie
        pwm.start(50)  # Start met een gemiddelde duty cycle

        print(f"Speelt {file_path} af...")
        try:
            for sample in samples:
                # Converteer sample naar duty cycle (0-100%)
                duty_cycle = (sample + 1) * 50
                pwm.ChangeDutyCycle(duty_cycle)
                time.sleep(1 / SAMPLE_RATE)
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
