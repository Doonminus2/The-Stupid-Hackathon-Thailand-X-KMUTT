import cv2
import os
import random

# Play a random video from a folder
def play_random_video(folder_path):
    # อ่านรายชื่อไฟล์ทั้งหมดในโฟลเดอร์
    try:
        files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
        if not files:
            print("No video files found in the folder.")
            return

        # เลือกไฟล์วิดีโอแบบสุ่ม
        video_file = random.choice(files)
        video_path = os.path.join(folder_path, video_file)
        print(f"Playing: {video_path}")

        # เปิดวิดีโอ
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error: Cannot open video file {video_file}.")
            return

        # เล่นวิดีโอ
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow('Video', frame)  # แสดงวิดีโอในหน้าต่าง

            # ปิดหน้าต่างเมื่อกดปุ่ม 'q'
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        cap.release()  # ปิดไฟล์วิดีโอ
        cv2.destroyAllWindows()  # ปิดหน้าต่างทั้งหมด

    except Exception as e:
        print(f"Error: {e}")

# ตัวอย่างการเรียกใช้งาน
if __name__ == "__main__":
    folder_path = "C:\\Users\\pie\\Desktop\\react\\hackethon\\videos"  # เปลี่ยนพาธให้ตรงกับโฟลเดอร์ของคุณ
    play_random_video(folder_path)
