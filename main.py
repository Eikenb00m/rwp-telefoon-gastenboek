from switch import Switch
from calling import CallingTone
import time

# Configuratie
SWITCH_PIN = 17  # GPIO-pin voor de schakelaar
PWM_PIN = 18     # GPIO-pin voor de beltoon
NUMBER_OF_CYCLES = 5  # Aantal cycles dat de beltoon moet spelen

# Initialisatie
switch = Switch(SWITCH_PIN)
calling_tone = CallingTone(PWM_PIN)

try:
    print("Wachten tot de hoorn wordt opgepakt...")
    while True:
        if switch.is_active():  # Controleer of de hoorn is opgepakt
            print("Hoorn opgepakt! Stop beltoon.")
            calling_tone.stop()  # Stop de beltoon
            break  # Verlaat de lus of voer andere logica uit
        else:
            print("Hoorn ligt neer. Start beltoon...")
            calling_tone.play_cycle(NUMBER_OF_CYCLES)
            time.sleep(1)  # Wacht even voordat je opnieuw controleert
except KeyboardInterrupt:
    print("Programma gestopt.")
finally:
    switch.cleanup()
    calling_tone.stop()
