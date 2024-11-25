import os
import time
import threading
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
audio_data = []  # Opslag voor audioframes
recording = False  # Status van de opname

# SPI- en MCP3008-configuratie
spi = busio.SPI(clock=SCK, MISO=MISO, MOSI=MOSI)
cs = digitalio.DigitalInOut(D10)  # GPIO10 (Pin 19) als CS
mcp = MCP3008(spi, cs)
chan = AnalogIn(mcp, 0)  # Gebruik kanaal 0 van de MCP3008

# Map maken voor opnames als deze nog niet bestaat
os.makedirs("opnames", exist_ok=True)

def record_audio():
    """
    Start met opnemen van audioframes.
    """
    global audio_data, recording
    audio_data = []  # Reset de audio-opslag
    recording = True
    print("Opname gestart! Typ 'stop' om te stoppen.")

    try:
        while recording:
            # Voeg data toe op basis van SAMPLE_RATE
            audio_data.append(chan.value)
            time.sleep(1 / SAMPLE_RATE)
    except Exception as e:
        print(f"Fout tijdens opnemen: {e}")

    print("Opname gestopt.")

def stop_recording():
    """
    Stop met opnemen en sla de audio op als WAV-bestand.
    """
    global recording
    recording = False  # Stop de opname-loop

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
            if not recording:
                threading.Thread(target=record_audio, daemon=True).start()
            else:
                print("Opname is al bezig!")
        elif command == "stop":
            if recording:
                stop_recording()
            else:
                print("Er is geen opname bezig!")
        elif command == "exit":
            if recording:
                print("Stop eerst de opname voordat je het programma afsluit.")
            else:
                print("Programma beëindigd.")
                break
        else:
            print("Onbekend commando. Typ 'start', 'stop' of 'exit'.")
