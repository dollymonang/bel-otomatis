import schedule
import time
import subprocess

def play_bell():
    audio_path = "bell.mp3"  # Ganti dengan file MP3 yang ada di Railway

    try:
        # Gunakan ffmpeg untuk memutar audio
        subprocess.run(["ffmpeg", "-i", audio_path, "-filter:a", "volume=1.0", "-f", "wav", "pipe:1"], check=True)
        print("Bel berbunyi!")
    except Exception as e:
        print(f"Error memutar bel: {e}")

# Jadwal Bel
schedule.every().day.at("16:30").do(play_bell)
schedule.every().day.at("16:50").do(play_bell)
schedule.every().day.at("17:00").do(play_bell)

print("Bel otomatis berjalan di Railway...")

while True:
    schedule.run_pending()
    time.sleep(30)
