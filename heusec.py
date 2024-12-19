from gpiozero import LED, Button
from signal import pause

# Configurazione dei pin
led = LED(16)
button = Button(17)

# Funzioni per accendere e spegnere il LED
def toggle_led():
    if led.is_lit:
        led.off()
    else:
        led.on()

# Collegamento del bottone all'azione
button.when_pressed = toggle_led

print("Programma avviato. Premi il pulsante per accendere o spegnere il LED.")
pause()
