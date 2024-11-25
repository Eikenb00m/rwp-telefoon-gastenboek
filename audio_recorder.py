import time
import numpy as np
from scipy.io.wavfile import write
import busio
import digitalio
from board import SCK, MISO, MOSI, D10  # Pas D10 aan naar jouw CS-pin (GPIO10)
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

# Maak de SPI-bus en MCP3008
spi = busio.SPI(clock=SCK, MISO=MISO, MOSI=MOSI)
cs = digitalio.DigitalInOut(D10)  # GPIO10 (Pin 19) als CS
mcp = MCP3008(spi, cs)

# Verbind een analoge ingang (bijv. kanaal 0)
chan = AnalogIn(mcp, MCP3008.P0)

# Opnameparameters
SAMPLE_RATE = 8000  # 8 kHz
DURATION = 5  # 5 seconden
NUM_SAMPLES = SAMPLE_RATE * DURATION
audio_data = []

print("Opname gestart...")
start_time = time.time()
while len(audio_data) < NUM_SAMPLES:
    audio_data.append(chan.value)
    time.sleep(1 / SAMPLE_RATE)  # Verzamel data op de juiste snelheid

print("Opname gestopt.")

# Normaliseer en converteer naar 16-bit
audio_array = np.array(audio_data, dtype=np.int16)
audio_array = (audio_array / max(audio_array) * 32767).astype(np.int16)

# Sla op als WAV-bestand
write("test_recording.wav", SAMPLE_RATE, audio_array)
print("Audio opgeslagen als test_recording.wav")
