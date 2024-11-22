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
        self.pwm = GPIO.PWM(self.pwm_pin, self.frequency)  # Stel de frequentie in
        self.is_running = False

    def play_cycle(self, cycles=1):
        """
        Speel de beltoon met opgegeven aantal cycles (aan/uit).
        :param cycles: Aantal keer dat de toon aan/uit moet gaan.
        """
        try:
            self.pwm.start(0)  # Start met 0% duty cycle
            self.is_running = True
            for i in range(cycles):
                print(f"Cycle {i + 1}: Toon aan...")
                self.pwm.ChangeDutyCycle(50)  # Zet de toon aan (50% duty cycle)
                time.sleep(2)  # Laat de toon 2 seconden aan staan
                print("Toon uit...")
                self.pwm.ChangeDutyCycle(0)  # Zet de toon uit
                time.sleep(2)  # Laat de toon 2 seconden uit staan
        finally:
            self.pwm.ChangeDutyCycle(0)  # Zorg dat de toon stopt na elke cycle
            self.is_running = False

    def stop(self):
        """
        Stop de toon en maak de GPIO vrij.
        """
        if self.is_running:
            self.pwm.ChangeDutyCycle(0)  # Zet de toon uit
            self.pwm.stop()  # Stop PWM
        GPIO.cleanup(self.pwm_pin)  # Maak alleen de gebruikte pin vrij
        print("Toon gestopt en GPIO vrijgegeven.")

if __name__ == "__main__":
    PWM_PIN = 18  # GPIO-pin voor PWM
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
