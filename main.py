import RPi.GPIO as GPIO
import time

PWM_PIN = 18  # GPIO 18 (BCM-modus)
FREQUENCY = 440  # Frequentie van de toon in Hz
DURATION = 5  # Duur van de toon in seconden

# GPIO-instellingen
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Start PWM op GPIO 18
pwm = GPIO.PWM(PWM_PIN, FREQUENCY)  # Stel frequentie in
pwm.start(50)  # Stel duty cycle in op 50%

print(f"Speel toon af: {FREQUENCY} Hz gedurende {DURATION} seconden.")
time.sleep(DURATION)  # Houd toon aan voor de opgegeven duur

# Stop PWM en maak GPIO schoon
pwm.stop()
GPIO.cleanup()
print("Geluid gestopt.")
