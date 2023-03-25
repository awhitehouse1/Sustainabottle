import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import datetime as dt
import time
from PIL.Image import Resampling
#Import pandas and matplotlib to use code.
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/
# Tkinter checkbox link: https://pythonbasics.org/tkinter-checkbox/
# Tkinter image tutorial link: https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/

# Menu Code - Start
# - https://www.tutorialspoint.com/python/tk_menu.htm - menus
# - https://www.pythontutorial.net/tkinter/tkinter-menu/ - submenus

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Water App")

# Set the window size
root.geometry("432x600")
root.resizable("False", "False")

#Add the image
img = Image.open("bottle.png")
img = img.resize((200,200), Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
label_image = tk.Label(image=img)
label_image.image = img
label_image.place(x=115,y=100)



button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, padx=5, pady=5)

def donothing():  # Placeholder Function
    x = 1

####
askTaskName = tk.Label(text="How much water did you drink since your last entry?", bg="white")
entry = tk.Entry()

askTaskName.pack()
entry.pack()
####

####
# Dropdown menu options
options = [
    "oz",
    "mL",
    "L"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("oz")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.pack()

def validate_water_entry():
    value = entry.get()
    entry.delete(0, END)
    if value.isnumeric() | value.isdecimal(): #Does not account for floats yet
        #call another method here
        print("Yellooooo")
    else:
        #Display an error label here
        print("HI")

# Create button, it will change label text
button = Button(root, text="Enter", command=validate_water_entry) #Can be repurposed into
button.pack()

# Create the buttons
button1 = tk.Button(button_frame, text="Button 1")
button1.pack(side=tk.LEFT, padx=5)

button2 = tk.Button(button_frame, text="Button 2")
button2.pack(side=tk.LEFT, padx=5)

button3 = tk.Button(button_frame, text="Button 3")
button3.pack(side=tk.LEFT, padx=5)

button4 = tk.Button(button_frame, text="Button 4")
button4.pack(side=tk.LEFT, padx=5)

# Run the main loop
root.mainloop()
