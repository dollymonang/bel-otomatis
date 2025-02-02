import schedule
import time
import pygame

pygame.mixer.init()

def play_bell():
    audio_path = "bell.mp3"  # Ganti dengan file nada bel
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

schedule.every().day.at("07:00").do(play_bell)
schedule.every().day.at("12:00").do(play_bell)
schedule.every().day.at("15:00").do(play_bell)

print("Bel otomatis berjalan di Railway...")

while True:
    schedule.run_pending()
    time.sleep(30)
