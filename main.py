from switch import Switch

SWITCH_PIN = 17
switch = Switch(SWITCH_PIN)

try:
    while True:
        if switch.is_active():
            print("Hoorn opgepakt!")
        else:
            print("Hoorn ligt neer.")
        time.sleep(1)
except KeyboardInterrupt:
    print("Programma gestopt.")
finally:
    switch.cleanup()
