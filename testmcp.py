import busio
import digitalio
import board
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

# Maak de SPI-bus aan
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# Stel de chip select (CS) pin in
cs = digitalio.DigitalInOut(board.D5)  # Pas aan naar de juiste pin

# Maak het MCP3008-object aan
mcp = MCP3008(spi, cs)

# Maak een AnalogIn-object voor kanaal 0
channel_0 = AnalogIn(mcp, 0)  # Gebruik 0 voor kanaal 0

# Lees en print de waarde van kanaal 0
raw_value = channel_0.value
voltage = channel_0.voltage
print(f"RAW waarde: {raw_value}, Voltage: {voltage:.2f}V")
