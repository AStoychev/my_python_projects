import os
import tkinter
from tkinter import *
import pygame
from PIL import ImageTk, Image
from pygame import mixer
from tkinter import filedialog, ttk

# You have to put а path to the music directory in row 172.

# colors
background = "#f6c0d0"  # pink
pink = "#ffe6e1"  # pink_women
black = "#1e1e1e"  # black
lemon_yellow = "#fcf45b"  # yellow
green = "#adc273"  # green
purple = "#d8e4ff"  # purple

window = Tk()
window.title("")
window.geometry("600x460")
window.configure(background=black)
window.resizable(width=FALSE, height=FALSE)


# events
def play_music():
    running = listbox.get(ACTIVE)
    running_song["text"] = running
    mixer.music.load(running)
    mixer.music.play()


def pause_music():
    try:
        playing = running_song["text"]
        index = songs.index(playing)
        if pause_button.config("text")[-1] == "1":
            pause_button.config(text=0, image=img_7)
            mixer.music.pause()
        else:
            pause_button.config(text="1", image=img_6)
            mixer.music.unpause()
    except:
        running_song["text"] = "First Choose Song"


def stop_music():
    mixer.music.stop()
    pause_button.config(text="1", image=img_6)
    mixer.music.unpause()
    running_song["text"] = "Stop"


def next_music(button):
    try:
        playing = running_song["text"]
        index = songs.index(playing)
        new_index = index
        if button == "forward":
            new_index = index + 1
        elif button == "backward":
            new_index = index - 1
        if new_index >= len(songs):
            new_index = 0
        if new_index < 0:
            new_index = len(songs) - 1
        playing = songs[new_index]
        mixer.music.load(playing)
        mixer.music.play()

        listbox.delete(0, END)
        show()
        listbox.select_set(new_index)
        running_song["text"] = playing
    except:
        running_song["text"] = "First Choose Song"


def music_volume(x):
    pygame.mixer.music.set_volume(slider.get())


def open_file():
    filepath = filedialog.askopenfilename(title="Choose your music", filetypes=[("music files", "*.mp3"),
                                                                                ("all files", "*.*")
                                                                                ])

    listbox.insert(END, filepath)


# frames
left_frame = Frame(window, width=300, height=300, bg=background)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(window, width=300, height=300, bg=pink)
right_frame.grid(row=0, column=1, padx=0)

down_frame = Frame(window, width=600, height=160, bg=purple)
down_frame.grid(row=1, column=0, columnspan=3, padx=1, pady=1)

# right_frame frame
listbox = Listbox(right_frame, selectmode=SINGLE, font=("Arial 9 bold"), width=39, bg=black, fg=lemon_yellow)
listbox.grid(row=0, column=0)

w = Scrollbar(right_frame, bg=lemon_yellow)
w.grid(row=0, column=1)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview())

# images
img_1 = Image.open("icon/background_music.jpg")
img_1 = img_1.resize((300, 300))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=350, image=img_1, padx=0, bg=black)
app_image.place(x=0, y=0)

img_2 = Image.open("icon/buttons/stop.jpg")
img_2 = img_2.resize((50, 50))
img_2 = ImageTk.PhotoImage(img_2)
stop_button = Button(down_frame, width=50, height=50, image=img_2, command=stop_music)
stop_button.place(x=150, y=50)

img_3 = Image.open("icon/buttons/play.jpg")
img_3 = img_3.resize((50, 50))
img_3 = ImageTk.PhotoImage(img_3)
play_button = Button(down_frame, width=50, height=50, image=img_3, command=play_music)
play_button.place(x=270, y=50)

img_4 = Image.open("icon/buttons/forward.jpg")
img_4 = img_4.resize((50, 50))
img_4 = ImageTk.PhotoImage(img_4)
forward_button = Button(down_frame, width=50, height=50, image=img_4, command=lambda: next_music("forward"))
forward_button.place(x=330, y=50)

img_5 = Image.open("icon/buttons/backward.jpg")
img_5 = img_5.resize((50, 50))
img_5 = ImageTk.PhotoImage(img_5)
backward_button = Button(down_frame, width=50, height=50, image=img_5, command=lambda: next_music("backward"))
backward_button.place(x=210, y=50)

img_6 = Image.open("icon/buttons/pause.jpg")
img_6 = img_6.resize((50, 50))
img_6 = ImageTk.PhotoImage(img_6)
pause_button = Button(down_frame, text="1", width=50, height=50, image=img_6, command=pause_music)
pause_button.pack(pady=10)
pause_button.place(x=390, y=50)

img_7 = Image.open("icon/buttons/continue.jpg")
img_7 = img_7.resize((50, 50))
img_7 = ImageTk.PhotoImage(img_7)

slider = ttk.Scale(down_frame, value=5, from_=0, to=1, cursor="gumby", orient=tkinter.VERTICAL, length=87,
                   command=music_volume)
slider.place(x=110, y=50)

add_misic_button = Button(down_frame, text="Add Music", background=pink, width=41, command=open_file)
add_misic_button.place(x=151, y=116)

line = Label(left_frame, width=100, height=1, padx=0, bg=black)
line.place(x=0, y=1)

line = Label(left_frame, width=100, height=1, padx=0, bg=black)
line.place(x=0, y=3)

running_song = Label(down_frame, text="Choose a Song and press Play", font=("Ivy 10"), width=75, height=1, padx=0,
                     bg=purple, fg=black, anchor=NW)
running_song.place(x=0, y=1)

# Add path to the directory
os.chdir(r"")
songs = os.listdir()


def show():
    for i in songs:
        listbox.insert(END, i)


show()

mixer.init()
music_state = StringVar()
music_state.set("Choose me!")
window.mainloop()
