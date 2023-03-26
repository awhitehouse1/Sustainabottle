# Import the required libraries
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from PIL.Image import Resampling
import re, datetime
from twilio.rest import Client
import keys

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

bg = Image.open("background.png")
bg = bg.resize((429, 600), Resampling.LANCZOS)
bg = ImageTk.PhotoImage(bg)
# Create Canvas
canvas1 = Canvas(main_menu, width=500,
                 height=800)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")


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


# MAIN MENU
askTaskName = Label(canvas1, text="Let's drink some water!", bg="white", font=('Arial', 12, 'bold'), pady=10)
entry = Entry(canvas1, width=10)

askTaskName.pack()
entry.place(x=150, y=50)

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
drop.place(x=230, y=50)

global allDrinkEntries
allDrinkEntries = []


def display_total_entries(value, measurement, currentTime):
    global allDrinkEntries
    drinkEntry = [None] * 4
    print(currentTime)
    drinkEntry[3] = str(currentTime)
    if measurement == 'oz':
        drinkEntry[0] = str(int(value))
        drinkEntry[1] = str(int(value) * 29.57353)  # milliliters = fluid ounces × 29.57353
        drinkEntry[2] = str(int(value) / 34)  # L = oz/33.814

    elif measurement == 'mL':
        drinkEntry[0] = str(int(value) / 29.57353)  # oz = mL/29.57353
        drinkEntry[1] = str(int(value))
        drinkEntry[2] = str(int(value) / 1000)  # L = mL/1000
    else:
        drinkEntry[0] = str(int(value) * 33.814)  # oz = L * 33.814
        drinkEntry[1] = str(int(value) * 1000)  # ml = L * 1000
        drinkEntry[2] = str(int(value))

    allDrinkEntries.append(drinkEntry)
    print(allDrinkEntries)


def display_total_saved(value, measurement):
    print(value)
    print(measurement)


def validate_water_entry():
    value = entry.get()
    entry.delete(0, END)
    if re.match("^(0|[1-9]\d*)?(\.\d+)?(?<=\d)$", value):
        currentTime = datetime.datetime.now()
        print(currentTime)
        display_total_saved(value, clicked.get())
        display_total_entries(value, clicked.get(), currentTime)
        clicked.set("oz")
        print("Yellooooo")
    else:
        # Display an error label here
        print("HI")


button = Button(canvas1, text="Enter", command=validate_water_entry, bg="#76b5a5", width=6, height=2)
button.place(x=200, y=90)

global total_saved
total_saved = 100
plastic_saved_number = Label(canvas1, text=str(total_saved), bg="white", font=('Arial', 80, 'bold'))
plastic_saved_number.place(x=165, y=225)

main_menu.pack(fill='both', expand=1)

# STATISTICS
label2 = Label(stats, text="in stats", foreground="blue")
label2.pack(side=LEFT)


# SETTINGS
bg_settings = Image.open("blank.png")
bg_settings = bg_settings.resize((429, 600), Resampling.LANCZOS)
bg_settings = ImageTk.PhotoImage(bg_settings)
# Create Canvas
canvas_settings = Canvas(settings, width=500,
                 height=800)

canvas_settings.pack(fill="both", expand=True)

# Display image
canvas_settings.create_image(0, 0, image=bg_settings,
                     anchor="nw")
is_on = False


def switch():
    global is_on
    if is_on:
        on_button.config(image=off)
        is_on = False
        number_entry.pack_forget()
        number_label.pack_forget()
        update_button.pack_forget()
        time_label.pack_forget()
        drop_time.pack_forget()
        mins_entry.pack_forget()
        hrs_entry.pack_forget()
    else:
        on_button.config(image=on)
        is_on = True
        number_label.place(x=25, y=210)
        number_entry.place(x=245, y=210)
        update_button.place(x=140, y=380)
        time_label.place(x=50, y=300)
        drop_time.place(x=310, y=300)
        mins_entry.place(x=260, y=300)
        hrs_entry.place(x=210, y=300)


def msg_send_time():
    mins = mins_entry.get()
    hrs = hrs_entry.get()
    phone_number = number_entry.get()
    if clicked2 == 'pm':
        hrs += 12
    curr_time = datetime.datetime.now()
    send_time = datetime.datetime(2023, 3, 26, int(hrs), int(mins))
    if curr_time > send_time:
        send_time = datetime.datetime(2023, 3, 26+1, int(hrs), int(mins))
    send_time = send_time.isoformat() + 'Z'

    client = Client(keys.account_sid, keys.auth_token)

    # message = client.messages.create(body="Remember to fill your water bottle!",
    #                                  from_=keys.twilio_number,
    #                                  to='+' + phone_number,
    #                                  schedule_type='fixed',
    #                                  send_at=send_time.isoformat() + 'Z',
    #                                  )

    message = client.messages.create(body="Remember to fill your water bottle!",
                                     from_=keys.twilio_number,
                                     to='+' + phone_number
                                     )



# Define Our Images
on = Image.open('on.png')
off = Image.open('off.png')
# Resize the image in the given (width, height)
on = on.resize((120, 70))
off = off.resize((120, 70))
# Conver the image in TkImage
on = ImageTk.PhotoImage(on)
off = ImageTk.PhotoImage(off)

on_button = Button(canvas_settings, image=off, bd=0, command=switch)
on_button.place(x=265, y=75)
notif_label = Label(canvas_settings, text="Recieve notifications", bg="white", font=('Arial', 15))
notif_label.place(x=40, y=100)
number_entry = Entry(canvas_settings, font=('Arial', 15), width=13)
number_label = Label(canvas_settings, text="Enter phone number:", bg="white", font=('Arial', 15))
time_label = Label(canvas_settings, text="Add reminder")

hrs_entry = Entry(canvas_settings, width=3, font=('Arial', 15))

mins_entry = Entry(canvas_settings, width=3, font=('Arial', 15))
time_options = ['am', 'pm']
clicked2 = StringVar()
clicked2.set("am")
drop_time = OptionMenu(canvas_settings, clicked2, *time_options)
time_label = Label(canvas_settings, text="Enter a time:", bg='white', font=('Arial', 15) )
update_button = Button(canvas_settings, text="Update Settings", bg="#76b5a5", font=('Arial', 15, 'bold'), command=msg_send_time, activebackground="#76b5a5")





# Add a button to switch between two frames
image_main = Image.open('main_menu_icon.png')
# Resize the image in the given (width, height)
image_main = image_main.resize((150, 75))
# Conver the image in TkImage
image_main = ImageTk.PhotoImage(image_main)
main_menu_btn = Button(root, image=image_main, width=150, bg="#76b5a5", command=change_to_main,
                       activebackground="#76b5a5")
main_menu_btn.place(x=145, y=520)

image_stats = Image.open('stats_icon.png')
# Resize the image in the given (width, height)
image_stats = image_stats.resize((80, 75))
# Conver the image in TkImage
image_stats = ImageTk.PhotoImage(image_stats)
stats_btn = Button(root, image=image_stats, width=150, bg="#76b5a5", command=change_to_stats,
                   activebackground="#76b5a5")
stats_btn.place(x=0, y=520)

image_settings = Image.open('settings_icon.png')
# Resize the image in the given (width, height)
image_settings = image_settings.resize((80, 75))
# Conver the image in TkImage
image_settings = ImageTk.PhotoImage(image_settings)
settings_btn = Button(root, image=image_settings, bg="#76b5a5", command=change_to_settings, width=150,
                      activebackground="#76b5a5")
settings_btn.place(x=290, y=520)

root.mainloop()
