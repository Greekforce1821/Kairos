# Important Libraries That The Program Uses

from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

# Important Information About The GUI

root=Tk()
root.title("Kairos Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

# Images For The GUI

image_icon=PhotoImage(file="images/logo.png")
root.iconphoto(False, image_icon)

# Assets For The GUI

Round_box=PhotoImage(file="images/rr1.png")
Label(root, image= Round_box, bg="#57adff").place(x=30, y=110)

# Added Labels For Each Temperature

label_one=Label(root, text="Temperature", font= ('Helvetica', 11), fg="white", bg="#203243")
label_one.place(x=50, y=120)

label_two=Label(root, text="Humidity", font= ('Helvetica', 11), fg="white", bg="#203243")
label_two.place(x=50, y=120)

label_three=Label(root, text="Pressure", font= ('Helvetica', 11), fg="white", bg="#203243")
label_three.place(x=50, y=120)

label_four=Label(root, text="Wind Speed", font= ('Helvetica', 11), fg="white", bg="#203243")
label_four.place(x=50, y=120)

label_fifth=Label(root, text="Description", font= ('Helvetica', 11), fg="white", bg="#203243")
label_fifth.place(x=50, y=120)


# Including A Search Box For The Cities

Search_image=PhotoImage(file="images/rr3.png")
image_me=Label(image=Search_image, bg="#57adff")
image_me.place(x=270, y=120)
cloud_image=PhotoImage(file="images/clouds.png")
weather_image=Label(root, image=cloud_image, bg="#203243")
weather_image.place(x=290, y=12)
