from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(17)
button = Button(2)


status = 0

led.on()
button.wait_for_press()
led.off()
if status == 0:
    led.off()
    button.wait_for_press()
    led.on()
    button.wait_for_press()
    led.off()
