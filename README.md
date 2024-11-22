I2S-configuratie
Schakel I2S in via het Raspberry Pi-configuratiemenu:

n
sudo raspi-config
Ga naar Interface Options > I2S > Enable.
Herstart je Raspberry Pi:

sudo reboot


Installeer essentiële pakketten
Je hebt een aantal extra tools nodig voor audio, GPIO en andere functionaliteiten:

Audio-tools
Voor het beheren van audio-invoer en -uitvoer:

bash
Code kopiëren
sudo apt install alsa-utils ffmpeg -y
alsa-utils:

Beheert audio-apparaten (zoals je I2S DAC en de microfoon).
Testopname en -afspelen: arecord en aplay.
ffmpeg:

Optioneel, voor audioconversies (bijvoorbeeld WAV naar MP3).