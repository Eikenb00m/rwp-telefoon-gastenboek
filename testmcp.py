import time
from gpiozero import MCP3008

# Initialiseer MCP3008 op kanaal 0
adc = MCP3008(channel=0)

try:
    while True:
        # Lees de analoge waarde (0 tot 1) en bereken de spanning
        waarde = adc.value  # Waarde tussen 0 en 1
        spanning = waarde * 3.3  # Omrekenen naar spanning
        print(f"Waarde: {waarde:.2f}, Spanning: {spanning:.2f}V")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Uitlezen gestopt.")
