# Important Libraries That The Program Uses

from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import requests
import pytz
from PIL import Image, ImageTk
from datetime import datetime
from datetime import timezone
import pytz.reference


# ---------------------------------------------

# Important Information About The GUI

root=Tk()
root.title("Kairos Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

# ----------------------------------------------

# Added The License File As A Drop-Down Menu
def License(): 
    Line_window = Toplevel(root)
    Line_window.title("License")
    Label(Line_window,text ="""MIT License

Copyright (c) 2022 Spyros Kokotos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""").pack()

# -----------------------------------------------

# Adding The Drop-Down Bar At The Top Of The GUI

menubar = Menu(root)
root.config(menu=menubar)
about = Menu(menubar)
menubar.add_cascade(label='Options', menu = about)
about.add_command(label="View Licenses", command = License)

# -----------------------------------------------

# def getWeather Fetches All The Valuable Information That Are Going To Be Used In The Kairos Program

def getWeather():
    city=textfield.get()

    geolocator= Nominatim(user_agent="geoapiExercises")
    location= geolocator.geocode(city)
    obj= TimezoneFinder()

    result= obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezn.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N{round(location.longitude, 4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # Here, By Using The API Key Which I Obtained From The OpenWeather Forecast Site, I Can Fetch Forecast From All Over The World

    api="https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=2cfed8cdd29d8e50088139f8cce8080e"
    json_data = requests.get(api).json()

    # Here, The Program Will Calculate And Represent The Current Temp, The Current Humidity, The Pressure, The WInd And Lastly The Description

    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    
    # Added The Text Output Inside The Box On The Left Side Of The GUI
    t.config(text=(temp,"°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description)

# ----------------------------------------------------

# Images For The GUI

image_icon=PhotoImage(file="images/logo.png")
root.iconphoto(False, image_icon)

# -----------------------------------------------------

# Assets For The GUI

Round_box=PhotoImage(file="images/rr1.png")
Label(root, image= Round_box, bg="#57adff").place(x=30, y=110)

# -----------------------------------------------------

# Added Labels For Each Temperature

label_one=Label(root, text="Temperature", font= ('Helvetica', 11), fg="white", bg="#203243")
label_one.place(x=50, y=120)

label_two=Label(root, text="Humidity", font= ('Helvetica', 11), fg="white", bg="#203243")
label_two.place(x=50, y=140)

label_three=Label(root, text="Pressure", font= ('Helvetica', 11), fg="white", bg="#203243")
label_three.place(x=50, y=160)

label_four=Label(root, text="Wind Speed", font= ('Helvetica', 11), fg="white", bg="#203243")
label_four.place(x=50, y=180)

label_fifth=Label(root, text="Description", font= ('Helvetica', 11), fg="white", bg="#203243")
label_fifth.place(x=50, y=200)

# -------------------------------------------------------

# Including A Search Box For The Cities

Search_image=PhotoImage(file="images/rr3.png")
image_search=Label(image=Search_image, bg="#57adff")
image_search.place(x=270, y=120)
cloud_image=PhotoImage(file="images/clouds.png")
weather_image=Label(root, image=cloud_image, bg="#203243")
weather_image.place(x=290, y=127)

# --------------------------------------------------------

# Including Text Input For The Search Box

textfield=tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=370, y=130)
textfield.focus()

# ---------------------------------------------------------

# Including A Magnifier As A Photo Of The Search Box

Search_icon=PhotoImage(file="images/search-icon.png")
image_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
image_icon.place(x=645, y=125)

# ---------------------------------------------------------

# Adding Support For Footer Boxes That They Will Be Used For Representing Data From The Forecast

footer_frame=Frame(root, width=900, height=180, bg="#212120")
footer_frame.pack(side=BOTTOM)

footer_box_one=PhotoImage(file="images/rr2.png")
footer_box_two=PhotoImage(file="images/rr2c.png")
footer_box_three=PhotoImage(file="images/rr2c.png")
footer_box_four=PhotoImage(file="images/rr2c.png")
footer_box_five=PhotoImage(file="images/rr2c.png")
footer_box_six=PhotoImage(file="images/rr2c.png")
footer_box_seven=PhotoImage(file="images/rr2c.png")

# ----------------------------------------------------------

# Each Footer Represents A Label At The Bottom Of The GUI

Label(footer_frame, image=footer_box_one, bg="#212120").place(x=30, y=20)
Label(footer_frame, image=footer_box_two, bg="#212120").place(x=300, y=20)
Label(footer_frame, image=footer_box_three, bg="#212120").place(x=400, y=20)
Label(footer_frame, image=footer_box_four, bg="#212120").place(x=500, y=20)
Label(footer_frame, image=footer_box_five, bg="#212120").place(x=600, y=20)
Label(footer_frame, image=footer_box_six, bg="#212120").place(x=700, y=20)
Label(footer_frame, image=footer_box_seven, bg="#212120").place(x=800, y=20)

# -----------------------------------------------------------

# Adding A Clock At The Top-Left Of The GUI

clock=Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)

# -----------------------------------------------------------

# Adding The Correct Timezone

timezn=Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezn.place(x=700, y=20)

# -----------------------------------------------------------

# Specifying The Latitude And The Longtitude

long_lat=Label(root, font=("Helvetica",20), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)

# ------------------------------------------------------------

# Creating Labels For Each Entry

t=Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=150, y=120)
h=Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=150, y=140)
p=Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=150, y=160)
w=Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=150, y=180)
d=Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=150, y=200)

# -------------------------------------------------------------















root.mainloop()