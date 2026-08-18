# cli_player.py — Notes

A simple command-line music player for macOS. It lists audio files in a folder and plays the one you pick.

## Imports
- `os` — used to read folder contents (`os.listdir`) and build file paths (`os.path.join`).
- `subprocess` — used to launch macOS's built-in `afplay` command as a separate process to actually play audio.

## `listSongs(directory_path)`
- Calls `os.listdir(directory_path)` to get all filenames in the folder as a Python list.
- Prints each one with a number (`1 : Song.mp3`, `2 : Song.mp3`, ...) using `enumerate(songs, start=1)`.

## `playSongs(number, directory_path)`
- Gets the same file list again with `os.listdir`.
- Checks that `number` is a valid index (between 1 and the number of songs); if not, prints an error and exits early via `return`.
- Builds the full path to the chosen song with `os.path.join(directory_path, songs[number - 1])`.
- Runs `subprocess.Popen(["afplay", song_path])` to play it — `Popen` starts the process without waiting for it to finish, so the script keeps running while the song plays.

## Program flow (bottom of file)
1. `listSongs('./songs')` — show all songs with numbers.
2. `input("Enter the song number: ")` — ask the user to pick one.
3. `playSongs(...)` — play the chosen song.

## Key idea
Earlier versions of this file used `subprocess.Popen(["ls", ...])` to list files by shelling out to the `ls` command. That was replaced with `os.listdir()`, which does the same job natively in Python — simpler, no need to parse text output.
