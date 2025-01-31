import pyautogui
import pygetwindow as gw
import time

pyautogui.FAILSAFE = False

def mute_spotify_when_ad():
    windows = gw.getWindowsWithTitle("Spotify Free")
    if windows:
        print("Spotify detected.")
    else:
        print("Spotify not detected (Make sure Spotify is open and not playing), exiting...")
        exit()
    previous_title = ""
    while True:
        win = windows[0]
        current_title = win.title
        is_ad = " - " not in current_title
        is_paused = "Spotify Free" in current_title
        if is_ad and not is_paused:
            print("Ad detected! Muting...")
            pyautogui.press("volumemute")
            while (is_ad):
                time.sleep(5)
                is_ad = " - " not in win.title
                is_paused = "Spotify Free" in win.title
            pyautogui.press("volumemute")
            print("Unmuting...")
            time.sleep(1)
            continue
        if previous_title != current_title and not is_paused:
            print(f"Now playing: {current_title}")
        previous_title = current_title
        time.sleep(3)
        
mute_spotify_when_ad()
