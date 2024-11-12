import RPi.GPIO as GPIO
import time

PWM_PIN = 18  # GPIO 18
TONEN = [220, 440, 880, 1760]  # Toonhoogtes in Hz
DUUR = 1  # Duur per toon in seconden

# GPIO-configuratie
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Start PWM
pwm = GPIO.PWM(PWM_PIN, 440)  # Start met een standaardfrequentie
pwm.start(50)  # Start met 50% duty cycle

try:
    for freq in TONEN:
        print(f"Speel {freq} Hz voor {DUUR} seconden...")
        pwm.ChangeFrequency(freq)  # Verander de frequentie
        time.sleep(DUUR)
    print("Test voltooid.")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("PWM gestopt en GPIO vrijgegeven.")
