import os
import numpy as np
import sounddevice as sd

SAMPLE_RATE = 44100  # Sample rate in Hz
DURATION = 5         # Duur van de toon in seconden
FREQUENCY = 440      # Frequentie van de toon in Hz

CONFIG_FILE = "/boot/config.txt"

def configure_pwm():
    """Controleer en configureer PWM op GPIO 18."""
    print("Controleer PWM-configuratie...")
    try:
        with open(CONFIG_FILE, "r") as file:
            config = file.read()

        pwm_settings = [
            "dtoverlay=pwm-2chan,pin=18,func=2",
            "dtoverlay=audremap,pins_18_19"
        ]

        missing_settings = [s for s in pwm_settings if s not in config]

        if missing_settings:
            print("PWM-configuratie ontbreekt. Toevoegen aan /boot/config.txt...")
            with open(CONFIG_FILE, "a") as file:
                for setting in missing_settings:
                    file.write(f"\n{setting}")
            print("PWM-configuratie toegevoegd. Systeem moet worden herstart.")
            os.system("sudo reboot")
        else:
            print("PWM-configuratie is correct.")
    except Exception as e:
        print(f"Fout bij het configureren van PWM: {e}")

def play_sound(frequency, duration):
    """Speel een eenvoudige toon af."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    print(f"Speel een toon van {frequency} Hz gedurende {duration} seconden.")
    sd.play(wave, samplerate=SAMPLE_RATE)
    sd.wait()
    print("Geluid klaar!")

if __name__ == "__main__":
    print("Start PWM-audio configuratie en test...")
    configure_pwm()  # Configureer PWM als nodig
    play_sound(FREQUENCY, DURATION)  # Speel een testtoon
