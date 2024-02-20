import tkinter as tk
from tkinter import font
import pygame
import os
import random

def play_song(song_path):
    if os.path.exists(song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
    else:
        print(f"File not found: {song_path}")

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    songs = [file for file in os.listdir(song_folder) if file.endswith('.mp3')]
    if songs:
        random_song = random.choice(songs)
        song_title.config(text=random_song)
        play_song(os.path.join(song_folder, random_song))
    else:
        print("No songs found in the folder.")

# Initialize pygame mixer
pygame.mixer.init()

# Define the folder where your songs are located
song_folder = r"C:\Users\Lambros\PycharmProjects\MusicPlayer\songs"

# Create the main window
root = tk.Tk()
root.title("Music Player")
root.geometry("400x300")  # Set the size of the window

# Custom font
custom_font = font.Font(family="Helvetica", size=12)

# Get the first song from the folder
initial_songs = [file for file in os.listdir(song_folder) if file.endswith('.mp3')]
initial_song = initial_songs[0] if initial_songs else "No Song Available"

# Create a label for the song title
song_title = tk.Label(root, text=initial_song, font=("Helvetica", 16), fg="blue")
song_title.pack(pady=10)

# Create Play, Stop, and Next buttons
play_button = tk.Button(root, text="Play", command=lambda: play_song(os.path.join(song_folder, song_title['text'])), font=custom_font, bg="green", fg="white")
play_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_song, font=custom_font, bg="red", fg="white")
stop_button.pack(pady=5)

next_button = tk.Button(root, text="Next", command=next_song, font=custom_font, bg="orange", fg="white")
next_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
