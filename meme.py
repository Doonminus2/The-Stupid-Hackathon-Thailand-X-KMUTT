import tkinter as tk
from PIL import Image, ImageTk
import os
import random
import sys

# หาเส้นทางของไฟล์ปัจจุบัน ไม่ว่าจะรันจาก .py หรือ .exe
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # เมื่อรันจาก .exe
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # เมื่อรันจาก .py
        return os.path.join(os.path.abspath("."), relative_path)

# ใช้งานฟังก์ชันนี้แทนเส้นทางเดิม
meme_folder = resource_path("imgage")
def show_meme():
    window = tk.Tk()
    window.title("Panic Button Activated!")
    
    # ทำให้หน้าต่างอยู่บนสุดเสมอ
    window.attributes('-topmost', True)
    # ทำให้เป็น fullscreen และไม่มีขอบ
    window.attributes('-fullscreen', True)
    # ซ่อนเคอร์เซอร์
    window.config(cursor="none")
    
    # โฟลเดอร์ที่เก็บรูป meme
    meme_folder = "C:\\Users\\pie\\Desktop\\react\\hackethon\\imgage"
    meme_files = [f for f in os.listdir(meme_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.jfif'))]
    
    if not meme_files:
        window.destroy()
        return
    
    try:
        # สุ่มเลือกรูป
        random_meme = random.choice(meme_files)
        image_path = os.path.join(meme_folder, random_meme)
        
        # โหลดรูปและปรับขนาดให้พอดีกับหน้าจอ
        img = Image.open(image_path)
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        # คำนวณขนาดที่ต้องปรับเพื่อให้รูปเต็มจอพอดี
        width_ratio = screen_width / img.width
        height_ratio = screen_height / img.height
        ratio = max(width_ratio, height_ratio)
        
        new_width = int(img.width * ratio)
        new_height = int(img.height * ratio)
        
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # ครอปส่วนเกินออกถ้าจำเป็น
        left = (new_width - screen_width) // 2 if new_width > screen_width else 0
        top = (new_height - screen_height) // 2 if new_height > screen_height else 0
        right = left + screen_width
        bottom = top + screen_height
        
        img = img.crop((left, top, right, bottom))
        photo = ImageTk.PhotoImage(img)
        
        # สร้าง canvas แทน label เพื่อแสดงรูปแบบเต็มจอ
        canvas = tk.Canvas(
            window,
            width=screen_width,
            height=screen_height,
            highlightthickness=0,  # ไม่มีขอบ
            bg='black'  # พื้นหลังดำ
        )
        canvas.pack(fill='both', expand=True)
        canvas.create_image(screen_width//2, screen_height//2, image=photo)
        
        # กำหนดเวลาปิดหน้าต่างภายใน 10 วินาที
        window.after(10000, lambda: window.destroy())
        
        # กด Esc เพื่อออก
        def exit_window(event=None):
            window.destroy()
        
        window.bind('<Escape>', exit_window)
        window.mainloop()
        
    except Exception as e:
        print(f"Error showing meme: {e}")
        window.destroy()

# เรียกใช้ฟังก์ชัน
show_meme()
