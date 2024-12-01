import time
import busio
import digitalio
from board import SCK, MISO, MOSI, D8  # Pas D8 aan naar jouw CS-pin
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

# SPI instellen
spi = busio.SPI(clock=SCK, MISO=MISO, MOSI=MOSI)
cs = digitalio.DigitalInOut(D8)  # Chip Select (GPIO8)
mcp = MCP3008(spi, cs)

# Kanaal 0 instellen
mic_input = AnalogIn(mcp, 0)

# Testloop
print("Lees de MCP3008...")
try:
    while True:
        print(f"RAW waarde: {mic_input.value}, Voltage: {mic_input.voltage:.2f}V")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Gestopt.")
