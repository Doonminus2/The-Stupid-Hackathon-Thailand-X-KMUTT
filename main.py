import time
import random
from pynput import keyboard
from meme import show_meme
from sound import play_sound


# Globals
last_activity = time.time()

# Activity detection
def on_activity(*args):
    global last_activity
    last_activity = time.time()

keyboard_listener = keyboard.Listener(on_press=on_activity)
keyboard_listener.start()





# Trigger chaos
def trigger_memes():
        show_meme()


# Main loop
while True:
    if time.time() - last_activity > 6:  # 10 minutes
        trigger_memes()
        last_activity = time.time()  # Reset activity
