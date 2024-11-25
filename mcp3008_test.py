import busio
import digitalio
from board import SCK, MISO, MOSI, D10  # Pas D5 aan naar jouw CS-pin
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

# Maak de SPI-bus
spi = busio.SPI(clock=SCK, MISO=MISO, MOSI=MOSI)

# Chip select pin
cs = digitalio.DigitalInOut(D5)

# Maak de MCP3008 ADC
mcp = MCP3008(spi, cs)

# Verbind een analoge ingang (bijv. kanaal 0)
chan = AnalogIn(mcp, MCP3008.P0)

print(f"Raw ADC waarde: {chan.value}")
print(f"Voltage: {chan.voltage:.2f}V")
