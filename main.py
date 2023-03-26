# Import the required libraries
from decimal import Decimal
from math import floor
from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
from PIL.Image import Resampling
import re, datetime

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
stats = Frame(root, bg="white")
settings = Frame(root, bg="white")

global total_saved
total_saved = 0

global num_bottles
num_bottles = 0

global text_size
text_size = 80

global label_image
label_image = []


bg = Image.open("background.png")
bg = bg.resize((429,600), Resampling.LANCZOS)
bg = ImageTk.PhotoImage(bg)
# Create Canvas
canvas1 = Canvas(main_menu, width=500,
                 height=800)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

def set_water_bottles():
    global label_image
    for label in label_image:
        label.destroy()
    if floor(num_bottles*2) >= 8:
        img1 = Image.open("checkmark.png")
        img1 = img1.resize((20, 20), Resampling.LANCZOS)
        img1 = ImageTk.PhotoImage(img1)
        check_mark_label = Label(stats, image=img1, bg="white")
        check_mark_label.image = img1
        check_mark_label.place(x=305, y=5)
        label_image.append(check_mark_label)
    for i in range(floor(num_bottles*2)):
        if i >= 8:
            break
        img = Image.open("bottle.png")
        img = img.resize((40, 80), Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        image_label = Label(stats, image=img, bg="white")
        image_label.image = img
        image_label.pack(side=LEFT, anchor=NW, padx=1)
        label_image.append(image_label)

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

askTaskName = Label(canvas1, text="How much water did you drink since your last entry?", bg="white")
entry = Entry(canvas1)

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
drop = OptionMenu(canvas1, clicked, *options)
drop.pack()

global allDrinkEntries
allDrinkEntries = []
def display_total_entries(value, measurement, currentTime):
    global allDrinkEntries, total_saved, num_bottles, plastic_saved_number, text_size
    drinkEntry = [None] * 4
    print(currentTime)
    drinkEntry[3] = str(currentTime)
    if measurement == 'oz':
        total_saved += Decimal(value)
        drinkEntry[0] = str(Decimal(value))
        drinkEntry[1] = str(Decimal(value) * Decimal(29.57353)) #milliliters = fluid ounces × 29.57353
        drinkEntry[2] = str(Decimal(value)/34) #L = oz/33.814

    elif measurement == 'mL':
        drinkEntry[0] = str(Decimal(value)/Decimal(29.57353)) #oz = mL/29.57353
        total_saved += Decimal(drinkEntry[0])
        drinkEntry[1] = str(Decimal(value))
        drinkEntry[2] = str(Decimal(value)/1000) #L = mL/1000
    else:
        drinkEntry[0] = str(Decimal(value) * Decimal(33.814)) #oz = L * 33.814
        total_saved = Decimal(drinkEntry[0])
        drinkEntry[1] = str(Decimal(value) * 1000) #ml = L * 1000
        drinkEntry[2] = str(Decimal(value))
    num_bottles = round(total_saved/16,2)
    allDrinkEntries.append(drinkEntry)
    plastic_saved_number.destroy()
    plastic_saved_number = Label(canvas1, text=str(num_bottles), bg="white", font=('Arial', 80, 'bold'))
    plastic_saved_number.place(x=165, y=225)
    while plastic_saved_number.winfo_reqwidth() > 216:
        text_size -= 1
        plastic_saved_number.configure(font=('Arial', text_size, 'bold'))
    set_water_bottles()
    print(allDrinkEntries)

def validate_water_entry():
    value = entry.get()
    entry.delete(0, END)
    if re.match("^(0|[1-9]\d*)?(\.\d+)?(?<=\d)$", value):
        currentTime = datetime.datetime.now()
        print(currentTime)
        display_total_entries(value, clicked.get(), currentTime)
    else:
        # Display an error label here
        print("HI")

button = Button(canvas1, text="Enter", command=validate_water_entry)
button.pack()

global plastic_saved_number
plastic_saved_number = Label(canvas1, text=str(num_bottles), bg="white", font=('Arial',text_size,'bold'))
plastic_saved_number.place(x=165,y=225)

main_menu.pack(fill='both', expand=1)

label2 = Label(stats, text="Daily Goal: 8 glasses of water", bg="white", font=('Arial', 16, 'bold'), padx=1)
label2.pack(side=TOP, anchor=NW)

label3 = Label(settings, text="in settings")
label3.pack(side=LEFT)


# Add a button to switch between two frames
image_main=Image.open('main_menu_icon.png')
# Resize the image in the given (width, height)
image_main=image_main.resize((150, 75))
# Conver the image in TkImage
image_main=ImageTk.PhotoImage(image_main)
main_menu_btn = Button(root, image=image_main, width=150, bg="#76b5a5", command=change_to_main, activebackground="#76b5a5")
main_menu_btn.place(x=145, y=520)

image_stats=Image.open('stats_icon.png')
# Resize the image in the given (width, height)
image_stats=image_stats.resize((80, 75))
# Conver the image in TkImage
image_stats=ImageTk.PhotoImage(image_stats)
stats_btn = Button(root, image=image_stats, width=150, bg="#76b5a5", command=change_to_stats, activebackground="#76b5a5")
stats_btn.place(x=0, y=520)

image_settings=Image.open('settings_icon.png')
# Resize the image in the given (width, height)
image_settings=image_settings.resize((80, 75))
# Convert the image in TkImage
image_settings=ImageTk.PhotoImage(image_settings)
settings_btn = Button(root, image=image_settings, bg="#76b5a5", command=change_to_settings, width=150, activebackground="#76b5a5")
settings_btn.place(x=290, y=520)

root.mainloop()