# Import the required libraries
from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
from PIL.Image import Resampling
import re

# Tkinter  tutorial link: https://realpython.com/python-gui-tkinter/
# Tkinter checkbox link: https://pythonbasics.org/tkinter-checkbox/
# Tkinter image tutorial link: https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/

# Menu Code - Start
# - https://www.tutorialspoint.com/python/tk_menu.htm - menus
# - https://www.pythontutorial.net/tkinter/tkinter-menu/ - submenus

# Create an instance of tkinter frame or window
root = Tk()

# Set the size of the window
root.geometry("432x600")
root.resizable("False", "False")
root.title("Water App")

# Create two frames in the window
main_menu = Frame(root)
stats = Frame(root)
settings = Frame(root)


# Define a function for switching the frames
def change_to_main():
    main_menu.pack(fill='both', expand=1)
    stats.pack_forget()
    settings.pack_forget()


def change_to_stats():
    stats.pack(fill='both', expand=1)
    main_menu.pack_forget()
    settings.pack_forget()


def change_to_settings():
    settings.pack(fill='both', expand=1)
    main_menu.pack_forget()
    stats.pack_forget()


# Add a heading logo in the frames

# MAIN MENU
# Add the image
img = Image.open("bottle.png")
img = img.resize((200, 200), Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
label_image = Label(main_menu, image=img)
label_image.image = img
label_image.place(x=115, y=100)

askTaskName = Label(main_menu, text="How much water did you drink since your last entry?", bg="white")
entry = Entry(main_menu)

askTaskName.pack()
entry.pack()

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
drop = OptionMenu(main_menu, clicked, *options)
drop.pack()


def display_total_saved(value, measurement):
    print(measurement)


def validate_water_entry():
    value = entry.get()
    entry.delete(0, END)
    if re.match("^(0|[1-9]\d*)?(\.\d+)?(?<=\d)$", value):
        display_total_saved(value, clicked.get())
        clicked.set("oz")
        print("Yellooooo")
    else:
        # Display an error label here
        print("HI")


button = Button(main_menu, text="Enter", command=validate_water_entry)  # Can be repurposed into
button.pack()


label2 = Label(stats, text="in stats", foreground="blue")
label2.pack(side=LEFT)

label3 = Label(settings, text="in settings")
label3.pack(side=LEFT)

# Add a button to switch between two frames
main_menu_btn = Button(root, text="Main Menu", height=7, width=20, command=change_to_main)
main_menu_btn.place(x=0, y=520)

stats_btn = Button(root, text="Stats", height=7, width=20, command=change_to_stats)
stats_btn.place(x=145, y=520)

settings_btn = Button(root, text="Settings", height=7, width=20, command=change_to_settings)
settings_btn.place(x=290, y=520)

root.mainloop()