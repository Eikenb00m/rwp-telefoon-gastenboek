import RPi.GPIO as GPIO
import sounddevice as sd
import numpy as np
import time

# Configuratie
HOORN_PIN = 17  # GPIO-pin verbonden met de schakelaar
TEST_FREQUENCY = 440  # Frequentie in Hz (A4-toon)
TEST_DURATION = 2  # Duur van het geluid in seconden

# GPIO-instellingen
GPIO.setmode(GPIO.BCM)  # BCM-pinindeling
GPIO.setup(HOORN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up omdat de schakelaar NC is

def play_test_sound(frequency, duration):
    """Speelt een testgeluid af met de gegeven frequentie en duur."""
    sample_rate = 44100  # Sample rate in Hz
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Sinusgolf
    sd.play(wave, samplerate=sample_rate)
    sd.wait()  # Wacht tot het geluid klaar is

print("Klaar! Neem de hoorn op om een geluid te horen.")

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
finally:
    GPIO.cleanup()  # Reset GPIO-instellingen
