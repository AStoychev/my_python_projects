import customtkinter
import requests
from bs4 import BeautifulSoup
from tkinter import Label, Frame, FALSE
from tkinter import Tk
from PIL import ImageTk, Image
from check_for_connection import internet_on
from data import url, cities
from weather_components import WeatherComponents

master = Tk()
master.title("Weather App")
master.iconbitmap("icon/weather.ico")
master.config(bg="white")
master.geometry("700x446")
master.resizable(width=FALSE, height=FALSE)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# frames
left_frame = Frame(master, width=350, height=460, bg="#CCFFFF")
left_frame.grid(row=0, column=0)
left_frame.grid_propagate(False)

right_frame = Frame(master, width=350, height=460, bg="#79D0C1")
right_frame.grid(row=0, column=1)
right_frame.grid_propagate(False)


def get_weather(city):
    page = requests.get(url[city])
    soup = BeautifulSoup(page.content, "html.parser")

    location = soup.find("h1", itemprop="name", class_="main-heading").text
    temp = soup.find("div", class_="h1 current-temp").text
    weather_prediction = soup.find("div", class_="current-description").text

    loc = WeatherComponents.town_location(location)
    temperature = WeatherComponents.town_temperature(temp)
    time_and_prediction = WeatherComponents.town_prediction(weather_prediction)
    time = time_and_prediction[0]
    prediction = time_and_prediction[1]

    location_label.config(text=loc)
    temperature_label.config(text=temperature)
    weather_prediction_label.config(text=prediction)
    time_label.config(text=time)


def create_city(text, command, y):
    city = customtkinter.CTkButton(master=master, compound="right",
                                   text=f"{text}", text_font=("Calibri bold", 15), text_color="#79D0C1",
                                   bg_color="#79D0C1", corner_radius=20, width=300, height=30,
                                   fg_color="#CCFFCC", hover_color="#C77C78",
                                   command=lambda: get_weather(f"{command}"))
    city.place(x=375, y=y)


for key, value in cities.items():
    create_city(key, value[0], value[1])

weather_symbols = []
image_x, image_y = 25, 385
for i in range(0, 4):
    pic = Image.open(f"icon/types/{i}.png")
    picture = pic.resize((30, 30))
    current_picture = ImageTk.PhotoImage(picture)
    weather_symbols.append(current_picture)
    image_x += 50
    weather_image = Label(right_frame, image=weather_symbols[i], bg="#79D0C1")
    weather_image.grid(row=1, column=1)
    weather_image.place(x=image_x, y=image_y)

# labels
location_label = Label(left_frame, font=("Calibri bold", 30), bg="#CCFFFF")
location_label.grid(row=0, sticky="N", padx=0, pady=41)
location_label.grid_propagate(False)

temperature_label = Label(left_frame, font=("Calibri bold", 70), bg="#CCFFFF", fg="blue")
temperature_label.grid(row=2, sticky="W", padx=70)

weather_prediction_label = Label(left_frame, font=("Calibri bold", 15), bg="#CCFFFF")
weather_prediction_label.place(x=100, y=50)
weather_prediction_label.grid(row=3, sticky="W", padx=70)

time_label = Label(left_frame, font=("Calibri bold", 15), bg="#CCFFFF")
time_label.grid(row=4, sticky="W", padx=130, pady=30)

weather = Image.open("icon/weather (1).png")
weather = weather.resize((70, 70))
weather = ImageTk.PhotoImage(weather)

Label(left_frame, image=weather, bg="#CCFFFF").grid(row=1, sticky="E", padx=150)

if internet_on() is True:
    pass
else:
    weather_prediction_label.config(font=("Calibri bold", 18), text="Check your internet connection")
    weather_prediction_label.grid(row=2, padx=18)

master.mainloop()
