The script works by reading the title of the Spotify application and pressing system mute when it detects ads playing.

How to use:
  1. Start Spotify application (Windows)
  2. Start the script (pythonw as a background process)
  3. Start playing songs

Assumptions (script will not work if any of the below are not satisfied): 
  1. There is only one window that contains "Spotify Free" in its title.
  2. Songs always contain " - " in its title name
  3. ads never contain " - " in its title name
  4. The user doesn't manually press the (system) mute button
