import busio
import digitalio
from board import SCK, MISO, MOSI, D8  # D8 = GPIO 8 (CS)
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

# Configureer SPI-bus en MCP3008
spi = busio.SPI(clock=SCK, MISO=MISO, MOSI=MOSI)
cs = digitalio.DigitalInOut(D8)
mcp = MCP3008(spi, cs)

# Verbind analoge ingang (kanaal 0)
mic_input = AnalogIn(mcp, 0)

print("Start met lezen van de microfoon...")
try:
    while True:
        print(f"RAW: {mic_input.value}, Voltage: {mic_input.voltage:.2f}V")
except KeyboardInterrupt:
    print("Test gestopt.")
