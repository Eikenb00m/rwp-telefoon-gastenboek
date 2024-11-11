import os
import RPi.GPIO as GPIO
import sounddevice as sd
import numpy as np
import time

# Configuratie
HOORN_PIN = 17  # GPIO-pin verbonden met de schakelaar
TEST_FREQUENCY = 440  # Frequentie in Hz (A4-toon)
TEST_DURATION = 2  # Duur van het geluid in seconden
VOLUME = 50  # Startvolume in procenten (0-100%)

# GPIO-instellingen
GPIO.setmode(GPIO.BCM)  # BCM-pinindeling
GPIO.setup(HOORN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up omdat de schakelaar NC is
GPIO.setup(18, GPIO.OUT)  # GPIO 18 configureren voor audio-uitvoer

def play_test_sound(frequency, duration):
    """Speelt een testgeluid af met de gegeven frequentie en duur."""
    sample_rate = 44100  # Sample rate in Hz
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Sinusgolf
    unmute_pwm()  # Zet de audio-uitvoer aan
    set_volume(VOLUME)  # Stel volume in
    sd.play(wave, samplerate=sample_rate)
    sd.wait()  # Wacht tot het geluid klaar is
    mute_pwm()  # Zet de audio-uitvoer uit

def mute_pwm():
    """Schakelt de audio-uitvoer uit."""
    os.system("amixer -c 0 sset 'PCM' mute")
    GPIO.setup(18, GPIO.IN)  # Zet GPIO 18 in input-modus om ruis te verminderen

def unmute_pwm():
    """Schakelt de audio-uitvoer weer in."""
    os.system("amixer -c 0 sset 'PCM' unmute")
    GPIO.setup(18, GPIO.OUT)  # Zet GPIO 18 terug in output-modus

def set_volume(volume):
    """Stel het volume in (0-100%)."""
    os.system(f"amixer -c 0 sset 'PCM' {volume}%")

def adjust_volume():
    """Pas het volume aan tijdens runtime."""
    global VOLUME
    try:
        new_volume = int(input("Voer nieuw volume in (0-100%): "))
        if 0 <= new_volume <= 100:
            VOLUME = new_volume
            print(f"Volume ingesteld op {VOLUME}%.")
        else:
            print("Volume moet tussen 0 en 100 liggen.")
    except ValueError:
        print("Ongeldige invoer. Voer een getal in tussen 0 en 100.")

print("Klaar! Neem de hoorn op om een geluid te horen.")
print("Druk op Ctrl+C om het programma te stoppen.")

try:
    while True:
        if GPIO.input(HOORN_PIN) == GPIO.HIGH:  # Hoorn is opgepakt (schakelaar geopend)
            print("Hoorn opgepakt! Geluid afspelen...")
            play_test_sound(TEST_FREQUENCY, TEST_DURATION)
            time.sleep(1)  # Wacht even voordat opnieuw wordt gecontroleerd
        else:
            print("Hoorn op de haak.")
        time.sleep(0.1)  # Vermijd overmatig CPU-gebruik
except KeyboardInterrupt:
    print("\nProgramma gestopt.")
    while True:
        adjust_volume()
finally:
    GPIO.cleanup()  # Reset GPIO-instellingen
    mute_pwm()  # Zorg dat de audio-uitvoer uitstaat
