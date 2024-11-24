# sound.py
import cv2
import os
import random

def play_random_video(folder_path):
    try:
        files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
        if not files:
            print("No video files found in the folder.")
            return

        video_file = random.choice(files)
        video_path = os.path.join(folder_path, video_file)
        print(f"Playing: {video_path}")

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error: Cannot open video file {video_file}.")
            return

        # สร้างหน้าต่างแบบ fullscreen
        cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow('Video', frame)

            # ปิดหน้าต่างเมื่อกดปุ่ม 'q' หรือ ESC
            key = cv2.waitKey(25) & 0xFF
            if key == ord('q') or key == 27:  # 27 is ESC key
                break

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {e}")