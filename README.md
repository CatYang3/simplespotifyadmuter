The script works by reading the title of the Spotify application and pressing desktop mute button when it detects ads playing.
(For songs only, not for podcasts)

Dependencies: PyGetWindow 0.0.9 (pip install PyGetWindow)

How to use:
  1. Start the script (via pythonw as a background process)
  2. Start playing songs

Assumptions (script will not work if any of the below are not satisfied): 
  1. There is only one window that contains "Spotify Free" in its title.
  2. Songs always contain " - " in its title name
  3. ads never contain " - " in its title name
  4. The user doesn't manually press the (system) mute button
