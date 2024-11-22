import numpy as np
import wave

# Parameters
sample_rate = 44100  # 44.1 kHz
duration = 5  # 5 seconden
frequency = 440.0  # 440 Hz (A4)

# Signaal genereren
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
signal = (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)

# WAV-bestand maken
with wave.open("sample.wav", "w") as f:
    f.setnchannels(1)  # Mono
    f.setsampwidth(2)  # 16-bit
    f.setframerate(sample_rate)
    f.writeframes(signal.tobytes())

print("sample.wav is succesvol gegenereerd!")
