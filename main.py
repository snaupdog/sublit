
import time
from pynput.keyboard import Controller

keyboard = Controller()  # Create the controller
time.sleep(5)
def type_string_with_delay(string):
    for character in string:  # Loop over each character in the string
        keyboard.type(character)  # Type the character
        delay = 0.001
        time.sleep(delay)  # Sleep for the amount of seconds generated

type_string_with_delay(""""sdasda  """)
