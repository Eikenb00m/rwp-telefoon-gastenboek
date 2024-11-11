import sounddevice as sd
import numpy as np

SAMPLE_RATE = 44100  # Sample rate in Hz
DURATION = 5         # Duur in seconden
FREQUENCY = 440      # Frequentie van de toon in Hz

# Genereer een sinusgolf
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
wave = 0.5 * np.sin(2 * np.pi * FREQUENCY * t)  # Correcte variabele naam

# Speel het geluid af
print("Speel toon af...")
sd.play(wave, samplerate=SAMPLE_RATE)
sd.wait()  # Wacht tot het geluid klaar is
print("Geluid klaar!")
