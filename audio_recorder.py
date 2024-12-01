import wave
import time
import numpy as np
from datetime import datetime

# Configuratie
SAMPLE_RATE = 8000  # 8 kHz
RECORD_SECONDS = 10  # Aantal seconden opnemen
CHANNEL = 0  # MCP3008 kanaal 0

# Voorbeeldfunctie voor MCP3008 (vervang met jouw MCP-code)
from adafruit_mcp3xxx.analog_in import AnalogIn
mic_input = AnalogIn(mcp, CHANNEL)

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
    # Normaliseer naar 16-bit
    sample = int((raw_value / 65535) * 32767)
    audio_data.append(sample)

# Schrijf data naar WAV-bestand
audio_array = np.array(audio_data, dtype=np.int16)
wavefile.writeframes(audio_array.tobytes())
wavefile.close()

print(f"Opname opgeslagen als: {filename}")
