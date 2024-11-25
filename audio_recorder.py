import os
import sounddevice as sd
import numpy as np
import wave
from datetime import datetime

# Parameters voor de opname
SAMPLE_RATE = 44100  # Sample rate in Hz
CHANNELS = 1  # Mono opname
DURATION = None  # Geen vaste tijdslimiet (loopt tot "stop")

# Maak de map 'opnames' als die nog niet bestaat
os.makedirs("opnames", exist_ok=True)

def record_audio():
    """
    Start met het opnemen van audio en sla het bestand op als WAV in de map 'opnames'.
    """
    print("Opnemen gestart! Typ 'stop' en druk op Enter om te stoppen.")

    recorded_data = []  # Hier slaan we de audioframes op

    try:
        def audio_callback(indata, frames, time, status):
            if status:
                print(f"Statusfout: {status}", flush=True)
            # Voeg inkomende data toe aan recorded_data
            recorded_data.append(indata.copy())
            # Toon de geluidsintensiteit in de terminal
            peak = np.abs(indata).max()
            print(f"Inputniveau: {int(peak * 100)}%", flush=True)

        # Start opname
        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            callback=audio_callback
        ):
            while True:
                user_input = input()  # Wacht op 'stop'
                if user_input.strip().lower() == "stop":
                    break

    except Exception as e:
        print(f"Fout tijdens opnemen: {e}")

    # Verwerk en sla de opname op
    print("Opname gestopt. Audio opslaan...")
    recorded_data = np.concatenate(recorded_data, axis=0)  # Combineer alle audioframes
    save_audio(recorded_data)
    print("Opname succesvol opgeslagen!")

def save_audio(data):
    """
    Sla de opgenomen audio op als WAV-bestand.
    :param data: Numpy-array met de audioframes.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"opnames/opname_{timestamp}.wav"

    # Schrijf de data naar een WAV-bestand
    with wave.open(filename, "w") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(data.astype(np.int16).tobytes())

    print(f"Bestand opgeslagen als: {filename}")

if __name__ == "__main__":
    print("Typ 'start' en druk op Enter om te beginnen met opnemen.")
    while True:
        command = input("Commando: ").strip().lower()
        if command == "start":
            record_audio()
        elif command == "exit":
            print("Programma beëindigd.")
            break
        else:
            print("Onbekend commando. Typ 'start' om te beginnen of 'exit' om af te sluiten.")
