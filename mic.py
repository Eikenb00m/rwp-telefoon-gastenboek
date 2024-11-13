import os
import pyaudio
import wave
import ffmpeg
from datetime import datetime

# Configuratie
RECORDS_DIR = "records"  # Map waar opnames worden opgeslagen
SAMPLE_RATE = 44100  # Sample rate in Hz
CHANNELS = 1  # Mono opname
CHUNK = 1024  # Buffergrootte
FORMAT = pyaudio.paInt16  # 16-bit audioformaat
RECORDING = False  # Status van opname

# Zorg dat de opslagmap bestaat
if not os.path.exists(RECORDS_DIR):
    os.makedirs(RECORDS_DIR)

def start_recording():
    """Start audio-opname."""
    global RECORDING
    audio = pyaudio.PyAudio()

    # Configuratie audio-invoer
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=SAMPLE_RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Opname gestart. Typ 'stop' om te stoppen.")
    frames = []

    try:
        while RECORDING:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Opname handmatig gestopt.")

    print("Opname beëindigd.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Sla opname op als WAV-bestand
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    wav_file = os.path.join(RECORDS_DIR, f"{timestamp}.wav")
    with wave.open(wav_file, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(b''.join(frames))

    print(f"Opname opgeslagen als {wav_file}")

    # Converteer naar MP3
    mp3_file = wav_file.replace(".wav", ".mp3")
    ffmpeg.input(wav_file).output(mp3_file).run(overwrite_output=True)
    os.remove(wav_file)  # Verwijder het originele WAV-bestand
    print(f"Opname geconverteerd naar MP3: {mp3_file}")

if __name__ == "__main__":
    while True:
        command = input("Typ 'start' om een opname te beginnen, 'stop' om te stoppen, of 'exit' om af te sluiten: ").strip().lower()
        if command == "start":
            RECORDING = True
            start_recording()
        elif command == "stop":
            RECORDING = False
        elif command == "exit":
            print("Programma afgesloten.")
            break
        else:
            print("Ongeldige invoer. Typ 'start', 'stop' of 'exit'.")
