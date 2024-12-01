import wave
import time
import numpy as np
from datetime import datetime
import busio
import digitalio
from board import SCK, MISO, MOSI, D8  # Pas D8 aan naar jouw CS-pin
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

# SPI-bus en MCP3008 configureren
spi = busio.SPI(clock=SCK, MISO=MISO, MOSI=MOSI)
cs = digitalio.DigitalInOut(D8)  # Chip Select (D8 = GPIO8, Pin 24)
mcp = MCP3008(spi, cs)

# Microfoon op kanaal 0
mic_input = AnalogIn(mcp, 0)

# Configuratie
SAMPLE_RATE = 44100  # 8 kHz
RECORD_SECONDS = 5  # Aantal seconden opnemen

# WAV-bestand configuratie
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"opnames/opname_{timestamp}.wav"
wavefile = wave.open(filename, 'w')
wavefile.setnchannels(1)  # Mono
wavefile.setsampwidth(2)  # 16-bits audio
wavefile.setframerate(SAMPLE_RATE)

print(f"Opnemen... ({RECORD_SECONDS} seconden)")
audio_data = []

# Start opnemen
start_time = time.time()
while time.time() - start_time < RECORD_SECONDS:
    raw_value = mic_input.value
    sample = int((raw_value / 65535) * 32767)
    audio_data.append(sample)
    time.sleep(1 / SAMPLE_RATE)  # Pauze tussen samples


# Schrijf data naar WAV-bestand
audio_array = np.array(audio_data, dtype=np.int16)
wavefile.writeframes(audio_array.tobytes())
wavefile.close()

print(f"Opname opgeslagen als: {filename}")
