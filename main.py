import os
import numpy as np
import sounddevice as sd

# Configuratie
FREQUENCY = 440  # Frequentie van de toon in Hz
DURATION = 2     # Duur van de toon in seconden
SAMPLE_RATE = 44100  # Sample rate in Hz

def play_test_tone(frequency, duration):
    """Speelt een testtoon af."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Sinusgolf
    sd.play(wave, samplerate=SAMPLE_RATE)
    sd.wait()

print("Speel een testtoon af...")
play_test_tone(FREQUENCY, DURATION)
