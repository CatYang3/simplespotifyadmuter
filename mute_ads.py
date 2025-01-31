import pyautogui
import pygetwindow as gw
import time

# Disable PyAutoGUI fail-safe
pyautogui.FAILSAFE = False

def get_spotify_window():
    for win in gw.getAllWindows():
        if "Spotify Free" in win.title:
            return win
    return None

def mute_spotify_when_ad():
    print("Waiting for Spotify...")
    win = None
    previous_title = ""

    while not win:  # First time opening Spotify
        win = get_spotify_window()
        time.sleep(3)
    print("Spotify detected! Starting ad detection...")
    
    while True:
        if not win or win.title == "":
            print("Spotify closed! Waiting for it to reopen...")
            while not win or win.title == "":
                time.sleep(3)
                win = get_spotify_window()
            print("Spotify detected! Resuming ad detection...")

        current_title = win.title
        is_ad = " - " not in current_title
        is_paused = "Spotify Free" in current_title

        if is_ad and not is_paused:
            print("Ad detected! Muting...")
            pyautogui.press("volumemute") #mute
            while is_ad:
                time.sleep(5)
                if not win or win.title == "":
                    break  # break out of the ad loop
                is_ad = " - " not in win.title
                is_paused = "Spotify Free" in win.title
            pyautogui.press("volumemute") #unmute
            print("Unmuting...")
            continue

        if previous_title != current_title and not is_paused:
            print(f"Now playing: {current_title}")

        previous_title = current_title
        time.sleep(3)

mute_spotify_when_ad()
