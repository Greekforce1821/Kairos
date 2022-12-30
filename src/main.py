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