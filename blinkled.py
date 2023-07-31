import machine
import time

# Configure GPIO pin for LED
LED_PIN = 23  # Change this value according to the GPIO pin you are using

# Configure pin as OUTPUT
led = machine.Pin(LED_PIN, machine.Pin.OUT)


# Function to set LED on or off
def set_led(state):
    led.value(state)


# Main loop for blinking
while True:
    set_led(1)  # Turn on LED
    time.sleep(1)  # Wait for 1 second
    set_led(0)  # Turn off LED
    time.sleep(1)  # Wait for another 1 second
