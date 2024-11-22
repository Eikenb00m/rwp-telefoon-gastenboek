import RPi.GPIO as GPIO
import time

class Switch:
    def __init__(self, pin):
        """
        Initialiseer de schakelaar op de opgegeven GPIO-pin.
        :param pin: GPIO-pin die de schakelaar gebruikt.
        """
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def is_active(self):
        """
        Controleer of de schakelaar is geactiveerd.
        :return: True als de schakelaar gesloten is (LOW), anders False.
        """
        return GPIO.input(self.pin) == GPIO.LOW

    def cleanup(self):
        """
        Maak de GPIO-pin vrij.
        """
        GPIO.cleanup(self.pin)

# Test de module zelfstandig
if __name__ == "__main__":
    SWITCH_PIN = 17  # Pas aan naar jouw GPIO-pin
    switch = Switch(SWITCH_PIN)

    try:
        print("Druk op de schakelaar om de status te zien. Druk Ctrl+C om te stoppen.")
        while True:
            if switch.is_active():
                print("Schakelaar is geactiveerd! (Hoorn opgepakt)")
            else:
                print("Schakelaar is niet geactiveerd. (Hoorn ligt neer)")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Programma gestopt.")
    finally:
        switch.cleanup()
