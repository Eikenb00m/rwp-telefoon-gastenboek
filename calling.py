import RPi.GPIO as GPIO
import time

class CallingTone:
    def __init__(self, pwm_pin, frequency=440):
        """
        Initialiseer de CallingTone generator.
        :param pwm_pin: GPIO-pin voor de PWM-uitgang.
        :param frequency: Frequentie van de toon in Hz.
        """
        self.pwm_pin = pwm_pin
        self.frequency = frequency
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, self.frequency)
        self.pwm.start(0)  # Start met duty cycle 0%

    def play_cycle(self, cycles=1):
        """
        Speel de beltoon met opgegeven aantal cycles (aan/uit).
        :param cycles: Aantal keer dat de toon aan/uit moet gaan.
        """
        for _ in range(cycles):
            print("Toon aan...")
            self.pwm.ChangeDutyCycle(50)  # 50% duty cycle
            time.sleep(2)  # Toon aan voor 2 seconden
            print("Toon uit...")
            self.pwm.ChangeDutyCycle(0)  # Toon uit
            time.sleep(2)  # Pauze voor 2 seconden

    def stop(self):
        """
        Stop de toon en maak de GPIO vrij.
        """
        self.pwm.stop()
        GPIO.cleanup()

# Test de module zelfstandig
if __name__ == "__main__":
    PWM_PIN = 18  # Pas aan naar jouw GPIO-pin
    calling_tone = CallingTone(PWM_PIN)

    try:
        print("Start beltoon test...")
        cycles = int(input("Voer het aantal cycles in: "))  # Vraag om aantal cycles
        calling_tone.play_cycle(cycles)
        print("Beltoon test voltooid.")
    except KeyboardInterrupt:
        print("Programma gestopt door gebruiker.")
    finally:
        calling_tone.stop()
