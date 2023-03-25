import tkinter as tk
from tkinter import *
import datetime as dt
import time
#Import pandas and matplotlib to use code.
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/
# Tkinter checkbox link: https://pythonbasics.org/tkinter-checkbox/

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

# Create button, it will change label text
button = Button(root, text="Enter", command=donothing()).pack() #Can be repurposed into
####

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
