import os
import time
import numpy as np
from scipy.io.wavfile import write
import busio
import digitalio
from board import SCK, MISO, MOSI, D10  # Pas D10 aan naar jouw CS-pin (GPIO10)
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn
from datetime import datetime

# Parameters
SAMPLE_RATE = 8000  # 8 kHz
DURATION = None  # Geen vaste tijdslimiet
audio_data = []  # Opslag voor audioframes

# SPI- en MCP3008-configuratie
spi = busio.SPI(clock=SCK, MISO=MISO, MOSI=MOSI)
cs = digitalio.DigitalInOut(D10)  # GPIO10 (Pin 19) als CS
mcp = MCP3008(spi, cs)
chan = AnalogIn(mcp, 0)  # Gebruik kanaal 0 van de MCP3008

# Map maken voor opnames als deze nog niet bestaat
os.makedirs("opnames", exist_ok=True)

def start_recording():
    """
    Start met opnemen van audioframes.
    """
    global audio_data
    audio_data = []  # Reset de audio-opslag
    print("Opname gestart! Typ 'stop' om te stoppen.")
    start_time = time.time()

    try:
        while True:
            # Voeg data toe op basis van SAMPLE_RATE
            audio_data.append(chan.value)
            time.sleep(1 / SAMPLE_RATE)
    except KeyboardInterrupt:
        print("\nOpname handmatig gestopt.")

def stop_recording():
    """
    Stop met opnemen en sla de audio op als WAV-bestand.
    """
    if not audio_data:
        print("Geen audio opgenomen!")
        return

    # Normaliseer en converteer naar 16-bit
    audio_array = np.array(audio_data, dtype=np.int16)
    audio_array = (audio_array / max(audio_array) * 32767).astype(np.int16)

    # Sla de opname op als WAV-bestand
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"opnames/opname_{timestamp}.wav"
    write(filename, SAMPLE_RATE, audio_array)
    print(f"Opname opgeslagen als: {filename}")

if __name__ == "__main__":
    print("Typ 'start' om een opname te starten, 'stop' om te stoppen, of 'exit' om af te sluiten.")

    while True:
        command = input("Commando: ").strip().lower()

        if command == "start":
            try:
                start_recording()
            except KeyboardInterrupt:
                print("\nOpname onderbroken. Typ 'stop' om te verwerken.")
        elif command == "stop":
            stop_recording()
        elif command == "exit":
            print("Programma beëindigd.")
            break
        else:
            print("Onbekend commando. Typ 'start', 'stop' of 'exit'.")
