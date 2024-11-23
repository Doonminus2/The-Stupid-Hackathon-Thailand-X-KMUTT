import time
from pynput import keyboard
from meme import show_meme

# Globals
last_activity = time.time()
keystroke_count = 0  # ตัวแปรนับจำนวนตัวอักษรที่พิมพ์

# Activity detection
def on_activity(key):
    global last_activity, keystroke_count
    last_activity = time.time()

    try:
        # ตรวจสอบว่า key ที่กดเป็นตัวอักษร (ไม่ใช่ Control หรือ Shift)
        if hasattr(key, 'char') and key.char is not None:
            keystroke_count += 1
            print(f"Keystroke count: {keystroke_count}")  # Debugging

            # หากพิมพ์ครบ 10 ตัวอักษร ให้เรียก show_meme และรีเซ็ตตัวนับ
            if keystroke_count >= 10:
                show_meme()
                keystroke_count = 0  # รีเซ็ตตัวนับ
    except AttributeError:
        pass

keyboard_listener = keyboard.Listener(on_press=on_activity)
keyboard_listener.start()

# Main loop
while True:
    time.sleep(0.1)  # ลดการใช้ทรัพยากร CPU
