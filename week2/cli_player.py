# import subprocess
# import os

# def listSongs(directory_path):
#     lists = subprocess.Popen(["ls", directory_path], stdout=subprocess.PIPE, text=True)
#     for i, line in enumerate(lists.stdout, start=1):
#         print(i, ":", line, end="")

# def playSongs(number, directory_path):
#     lists = subprocess.Popen(["ls", directory_path], stdout=subprocess.PIPE, text=True)
#     song_path = None
#     for i, line in enumerate(lists.stdout, start=1):
#         if number == i:
#             song_path = directory_path + "/" + line.strip()
#             break

#     if song_path is None:
#         print("No song with that number.")
#         return

#     subprocess.Popen(["afplay", song_path])


# listSongs('./songs')
# playSongs(int(input("Enter the song number: ")), "./songs")

import subprocess
import os

def listSongs(directory_path):
    songs = os.listdir(directory_path)
    for i, song in enumerate(songs, start=1):
        print(i, ":", song)

def playSongs(number, directory_path):
    songs = os.listdir(directory_path)
    if number < 1 or number > len(songs):
        print("No song with that number.")
        return
    song_path = os.path.join(directory_path, songs[number - 1])
    subprocess.Popen(["afplay", song_path])


listSongs('./songs')
playSongs(int(input("Enter the song number: ")), "./songs")
