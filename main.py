import vlc
import time

# Pad naar het MP3-bestand
MP3_FILE = "test.mp3"  # Vervang door je bestandspad

# Initialiseer VLC-speler
player = vlc.MediaPlayer(MP3_FILE)

# Speel het MP3-bestand af
print(f"Speelt {MP3_FILE} af...")
player.play()

# Wacht totdat het bestand is afgespeeld
time.sleep(1)  # Geef VLC de tijd om te starten
while player.is_playing():
    time.sleep(1)

print("Afspelen voltooid.")
