import os

def set_volume(volume):
    """
    Stel het volume in via amixer.
    :param volume: Volumepercentage (0-100).
    """
    if 0 <= volume <= 100:
        os.system(f"amixer set 'PCM' {volume}%")
        print(f"Volume ingesteld op {volume}%")
    else:
        print("Volume moet tussen 0 en 100 liggen.")

if __name__ == "__main__":
    print("Voer het gewenste volume in (0-100):")
    try:
        vol = int(input())
        set_volume(vol)
    except ValueError:
        print("Ongeldige invoer. Voer een getal in tussen 0 en 100.")
