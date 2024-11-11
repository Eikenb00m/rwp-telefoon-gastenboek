import os
import numpy as np
import sounddevice as sd

# Configuratie
SAMPLE_RATE = 44100  # Sample rate in Hz
DURATION = 5         # Duur van de toon in seconden
FREQUENCY = 440      # Frequentie van de toon in Hz
DEFAULT_VOLUME = 80  # Standaardvolume in procenten (0-100%)

def play_sound(frequency, duration):
    """Speel een toon af."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    print(f"Speelt {frequency} Hz toon voor {duration} seconden...")
    sd.play(wave, samplerate=SAMPLE_RATE)
    sd.wait()
    print("Klaar met afspelen.")

def set_volume(volume):
    """Stel het volume in (0-100%)."""
    os.system(f"amixer -c 0 sset 'PCM' {volume}%")
    print(f"Volume ingesteld op {volume}%.")

def adjust_volume():
    """Pas het volume aan via invoer."""
    try:
        new_volume = int(input("Voer nieuw volume in (0-100%): "))
        if 0 <= new_volume <= 100:
            set_volume(new_volume)
        else:
            print("Ongeldig volume. Voer een waarde in tussen 0 en 100.")
    except ValueError:
        print("Ongeldige invoer. Probeer opnieuw.")

# Start van het script
if __name__ == "__main__":
    print("Script gestart.")
    set_volume(DEFAULT_VOLUME)  # Stel standaardvolume in

    while True:
        print("\n1: Speel geluid af")
        print("2: Pas volume aan")
        print("3: Stop script")
        keuze = input("Kies een optie: ")

        if keuze == "1":
            play_sound(FREQUENCY, DURATION)
        elif keuze == "2":
            adjust_volume()
        elif keuze == "3":
            print("Script gestopt.")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
