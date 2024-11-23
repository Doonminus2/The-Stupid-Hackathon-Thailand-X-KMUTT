from pygame import mixer
# Play sound
def play_sound():
    mixer.init()
    mixer.music.load("C:\\Users\\pie\\Desktop\\react\\hackethon\\LastRIZZDAYNIGHT.mp3")
    mixer.music.play()
