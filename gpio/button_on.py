from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(17)
led_1 = LED(27)
led_2 = LED(22)
button = Button(2)

while True:
    led_1.on()
    sleep(1)
    led_1.off()
    sleep(0.1)
    led.on()
    sleep(1)
    led.off()
    sleep(0.1)
    led_2.on()
    sleep(1)
    led_2.off()
    sleep(0.1)
    if button.when_pressed:
        led_.





# button.when_released = led_1.off

pause()