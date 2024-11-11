import sounddevice as sd
import numpy as np

# Configuratie
FREQUENCY = 440  # Frequentie van de toon in Hz (A4-toon)
DURATION = 5     # Duur van de toon in seconden
SAMPLE_RATE = 44100  # Sample rate in Hz

def play_simple_sound(frequency, duration):
    """Speelt een simpele toon af."""
    print(f"Speel een toon af van {frequency} Hz voor {duration} seconden.")
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Genereer een sinusgolf
    sd.play(wave, samplerate=SAMPLE_RATE)  # Speel het geluid af
    sd.wait()  # Wacht tot het geluid klaar is
    print("Geluid is klaar.")

# Speel een geluid af
play_simple_sound(FREQUENCY, DURATION)
