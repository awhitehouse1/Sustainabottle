import tkinter as tk
import datetime as dt
import time
#Import pandas and matplotlib to use code.
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/
# Tkinter checkbox link: https://pythonbasics.org/tkinter-checkbox/

window = tk.Tk()

window.title("Water App")
window.geometry("800x600")
window.config(bg="white")
window.mainloop()
# Menu Code - Start
# - https://www.tutorialspoint.com/python/tk_menu.htm - menus
# - https://www.pythontutorial.net/tkinter/tkinter-menu/ - submenus
def donothing():  # Placeholder Function
    filewin = tk.Toplevel(window)
    button = tk.Button(filewin, text="Do nothing button")
    button.pack()