import spidev
import time

# MCP3008-configuratie
SPI_CHANNEL = 0  # Gebruik SPI kanaal 0 (CE0)
spi = spidev.SpiDev()
spi.open(0, SPI_CHANNEL)  # Bus 0, apparaat 0
spi.max_speed_hz = 1350000

def read_adc(channel):
    """Lees data van MCP3008 ADC."""
    if channel < 0 or channel > 7:
        raise ValueError("Kanaal moet tussen 0 en 7 liggen.")
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    print("Lees microfoonwaarden van kanaal 0. Druk Ctrl+C om te stoppen.")
    while True:
        mic_value = read_adc(0)  # Lees kanaal 0
        print(f"Microfoonwaarde: {mic_value}")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Test gestopt.")
finally:
    spi.close()
