import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk

import datetime as dt
import time
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
img = Image.open("bottle.jpg")
img = img.resize((50,50), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
label_image = tk.Label(image=img)
label_image.image = img
label_image.place(x=216,y=300)



button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, padx=5, pady=5)

####
askTaskName = tk.Label(text="Enter the name of the task below.", bg="white")
entry = tk.Entry()

askTaskName.pack()
entry.pack()
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
