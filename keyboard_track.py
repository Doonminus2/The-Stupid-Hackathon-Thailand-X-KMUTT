import time
from pynput import keyboard
from collections import deque

# Global variables
keystrokes = deque()
is_window_shown = False
window = None


def on_press(key):
    global keystrokes, is_window_shown
    current_time = time.time()
    keystrokes.append(current_time)

    # เก็บแค่การพิมพ์ใน 10 วินาทีล่าสุด
    while keystrokes and current_time - keystrokes[0] > 5:
        keystrokes.popleft()

    # คำนวณ WPM
    if len(keystrokes) >= 2:
        duration = current_time - keystrokes[0]
        if duration > 0:
            chars = len(keystrokes)
            wpm = (chars * 60) / (duration * 5)  # 1 word = 5 chars

            if wpm > 50 and duration >= 5:

# เริ่มการตรวจจับการพิมพ์
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Main loop
while True:
    time.sleep(1)