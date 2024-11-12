import RPi.GPIO as GPIO
import wave
import numpy as np
import time

# Configuratie
PWM_PIN = 18  # GPIO 18 voor PWM
WAV_FILE = "test.wav"  # Pad naar het WAV-bestand
BUFFER_SIZE = 1024  # Aantal samples om tegelijk te verwerken

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

def normalize_samples(samples):
    """Normaliseer samples naar een bereik van 0 tot 100."""
    samples = samples - np.min(samples)  # Schuif naar positief bereik
    samples = samples / np.ptp(samples)  # ptp = max - min (bereik normalisatie)
    return samples * 100  # Schaal naar 0-100%

def play_wav(file_path):
    """Speel een WAV-bestand realtime af via PWM."""
    with wave.open(file_path, "rb") as wav_file:
        # Haal WAV-parameters op
        num_channels = wav_file.getnchannels()
        sample_rate = wav_file.getframerate()

        print(f"Kanalen: {num_channels}, Sample rate: {sample_rate} Hz")

        # Start PWM
        pwm = GPIO.PWM(PWM_PIN, sample_rate)
        pwm.start(0)  # Start met duty cycle 0%

        print("Afspelen gestart...")
        try:
            while True:
                # Lees een buffer aan samples
                frames = wav_file.readframes(BUFFER_SIZE)
                if not frames:  # Stop als het einde van het bestand is bereikt
                    break
                
                # Converteer stereo naar mono en normaliseer
                samples = stereo_to_mono(frames, num_channels)
                samples = normalize_samples(samples)

                # Speel de samples af
                for sample in samples:
                    pwm.ChangeDutyCycle(sample)  # Pas duty cycle aan
                    time.sleep(1 / sample_rate)  # Houd de sample rate aan
        except KeyboardInterrupt:
            print("Afspelen onderbroken.")
        finally:
            pwm.stop()

# Start het afspelen
try:
    play_wav(WAV_FILE)
finally:
    GPIO.cleanup()
    print("Afspelen voltooid.")
