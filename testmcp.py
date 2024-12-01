import busio
import digitalio
from board import SCK, MISO, MOSI, D8
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

# Initialiseer de SPI-bus
spi = busio.SPI(clock=SCK, MISO=MISO, MOSI=MOSI)
# Stel de Chip Select (CS) pin in
cs = digitalio.DigitalInOut(D8)  # D8 komt overeen met GPIO14

# Maak een MCP3008 object aan
mcp = MCP3008(spi, cs)

# Maak een AnalogIn object voor kanaal 0
channel_0 = AnalogIn(mcp, MCP3008.P0)

# Lees en print de waarde van kanaal 0
raw_value = channel_0.value
voltage = channel_0.voltage
print(f"RAW waarde: {raw_value}, Voltage: {voltage:.2f}V")
