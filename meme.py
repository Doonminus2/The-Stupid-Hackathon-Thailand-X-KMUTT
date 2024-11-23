import tkinter as tk
from PIL import Image, ImageTk
import os
import random

def show_meme():
    window = tk.Tk()
    window.title("Panic Button Activated!")
    window.attributes('-topmost', True)
    # ปิด maximize button
    window.resizable(False, False)
    
    # โฟลเดอร์ที่เก็บรูป meme
    meme_folder = "C:\\Users\\pie\\Desktop\\react\\hackethon\\imgage"
    meme_files = [f for f in os.listdir(meme_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.jfif'))]
    
    if not meme_files:
        return
    
    # สุ่มเลือกรูป
    random_meme = random.choice(meme_files)
    image_path = os.path.join(meme_folder, random_meme)
    
    # โหลดรูปตามขนาดจริง
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)
    
    # แสดงรูป
    label = tk.Label(window, image=photo)
    label.image = photo  # เก็บ reference ไว้ป้องกัน garbage collection
    label.pack()
    
    # กด Esc เพื่อออก
    def exit_window(event=None):
        window.destroy()
    
    window.bind('<Escape>', exit_window)
    
    # สุ่มตำแหน่งหน้าต่าง
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    
    # หาขนาดหน้าจอ
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # สุ่มตำแหน่ง x, y โดยให้หน้าต่างอยู่ในหน้าจอทั้งหมด
    x = random.randint(0, max(0, screen_width - width))
    y = random.randint(0, max(0, screen_height - height))
    
    window.geometry(f'{width}x{height}+{x}+{y}')
    
    window.mainloop()