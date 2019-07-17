from gpiozero import LED
from time import sleep


led = LED(17)
led_1 = LED(27)
led_2 = LED(22)

while True:
    led_1.on()
    sleep(10)
    led_1.off()
    sleep(0.1)
    led.on()
    sleep(10)
    led.off()
    sleep(0.1)
    led_2.on()
    sleep(10)
    led_2.off()
    sleep(0.1)



