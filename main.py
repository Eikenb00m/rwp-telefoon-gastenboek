from switch import Switch  # Zorg dat de Switch-module correct is geïmporteerd
import time  # Voeg dit toe

SWITCH_PIN = 17
switch = Switch(SWITCH_PIN)

try:
    while True:
        if switch.is_active():
            print("Hoorn opgepakt!")
        else:
            print("Hoorn ligt neer.")
        time.sleep(1)  # Tijdelijke pauze om CPU-belasting te minimaliseren
except KeyboardInterrupt:
    print("Programma gestopt.")
finally:
    switch.cleanup()
