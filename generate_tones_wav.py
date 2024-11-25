import numpy as np
import wave

def generate_tone(frequency, duration, sample_rate=44100):
    """
    Genereer een sinus-toon met een specifieke frequentie en duur.
    :param frequency: Frequentie in Hz.
    :param duration: Duur in seconden.
    :param sample_rate: Sample rate in Hz (standaard 44100).
    :return: Numpy-array met audio samples.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)
    return signal

# Parameters
sample_rate = 44100  # 44.1 kHz
tones = [
    (440, 1),  # 440 Hz voor 1 seconde
    (550, 1),  # 550 Hz voor 1 seconde
    (660, 1),  # 660 Hz voor 1 seconde
    (770, 1),  # 770 Hz voor 1 seconde
    (880, 1),  # 880 Hz voor 1 seconde
]
stereo = True  # Zet op False voor mono

# Combineer tonen in één signaal
audio = np.concatenate([generate_tone(freq, dur, sample_rate) for freq, dur in tones])

# Als stereo, kopieer naar twee kanalen
if stereo:
    audio = np.column_stack((audio, audio))

# WAV-bestand schrijven
filename = "tones.wav"
with wave.open(filename, "w") as wav_file:
    wav_file.setnchannels(2 if stereo else 1)  # Stereo of mono
    wav_file.setsampwidth(2)  # 16-bit audio
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(audio.tobytes())

print(f"{filename} is succesvol gegenereerd!")
