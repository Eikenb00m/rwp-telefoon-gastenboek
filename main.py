import pygame
import time

# Initialiseer pygame mixer
pygame.mixer.init()

# Pad naar het MP3-bestand
MP3_FILE = "test.mp3"  # Vervang dit door de naam van je MP3-bestand

# Laad het MP3-bestand
try:
    pygame.mixer.music.load(MP3_FILE)
    print(f"Afspelen van bestand: {MP3_FILE}")
except pygame.error as e:
    print(f"Fout bij het laden van bestand: {e}")
    exit()

# Speel het MP3-bestand af
pygame.mixer.music.play()

# Wacht tot het bestand is afgespeeld
while pygame.mixer.music.get_busy():
    time.sleep(1)

print("Afspelen voltooid.")
