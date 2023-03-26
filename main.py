# Import the required libraries
from decimal import Decimal
from math import floor
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

global daily_count
daily_count = 0

global allDrinkEntries
allDrinkEntries = []

global list_of_badges
list_of_badges = []


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

def set_water_bottles():
    global label_image, daily_count
    daily_num_bottles = daily_count/16
    for label in label_image:
        label.destroy()
    if floor(daily_num_bottles*2) >= 8:
        img1 = Image.open("checkmark.png")
        img1 = img1.resize((20, 20), Resampling.LANCZOS)
        img1 = ImageTk.PhotoImage(img1)
        check_mark_label = Label(stats, image=img1, bg="white")
        check_mark_label.image = img1
        check_mark_label.place(x=280, y=5)
        label_image.append(check_mark_label)
    for i in range(floor(daily_num_bottles*2)):
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
    list_badges()

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


def display_total_entries(value, measurement, currentTime):
    global allDrinkEntries, total_saved, num_bottles, plastic_saved_number, text_size, daily_count
    drinkEntry = [None] * 4
    drinkEntry[3] = str(currentTime)
    if measurement == 'oz':
        drinkEntry[0] = str(Decimal(value))
        drinkEntry[1] = str(Decimal(value) * Decimal(29.57353)) #milliliters = fluid ounces × 29.57353
        drinkEntry[2] = str(Decimal(value)/34) #L = oz/33.814

    elif measurement == 'mL':
        drinkEntry[0] = str(Decimal(value)/Decimal(29.57353)) #oz = mL/29.57353
        drinkEntry[1] = str(Decimal(value))
        drinkEntry[2] = str(Decimal(value)/1000) #L = mL/1000
    else:
        drinkEntry[0] = str(Decimal(value) * Decimal(33.814)) #oz = L * 33.814
        drinkEntry[1] = str(Decimal(value) * 1000) #ml = L * 1000
        drinkEntry[2] = str(Decimal(value))
    total_saved += Decimal(drinkEntry[0])

    num_bottles = round(total_saved/16,2)
    allDrinkEntries.append(drinkEntry)

    plastic_saved_number.destroy()
    plastic_saved_number = Label(canvas1, text=str(num_bottles), bg="white", font=('Arial', 80, 'bold'))
    plastic_saved_number.place(x=165, y=225)
    while plastic_saved_number.winfo_reqwidth() > 216:
        text_size -= 1
        plastic_saved_number.configure(font=('Arial', text_size, 'bold'))
    daily_count = 0
    current_day = datetime.datetime.now()
    current_day = str(current_day).split(" ")
    current_day = current_day[0]
    for val in allDrinkEntries:
        logged_day = val[3].split(" ")
        bottle_day = logged_day[0]
        if bottle_day == current_day:
            daily_count += Decimal(val[0])
    set_water_bottles()

def validate_water_entry():
    value = entry.get()
    entry.delete(0, END)
    if re.match("^(0|[1-9]\d*)?(\.\d+)?(?<=\d)$", value):
        currentTime = datetime.datetime.now()
        display_total_entries(value, clicked.get(), currentTime)
    else:
        # Display an error label here
        error_label = Label(canvas1, text="Please enter a valid number.", bg="white", font=('Arial',12), foreground="red")
        error_label.place(x=110,y=105)
        canvas1.after(2000, error_label.destroy)


button = Button(canvas1, text="Enter", command=validate_water_entry, bg="#76b5a5", width=6, height=2)
button.place(x=200, y=90)

plastic_saved_number = Label(canvas1, text=str(total_saved), bg="white", font=('Arial', 80, 'bold'))
plastic_saved_number.place(x=165, y=225)

main_menu.pack(fill='both', expand=1)

# STATISTICS

label2 = Label(stats, text="Daily Goal: 8 cups of water", bg="white", font=('Arial', 16, 'bold'), padx=1)
label2.pack(side=TOP, anchor=NW)



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
    global number_entry
    global number_label
    global time_label
    global hrs_entry
    global mins_entry
    global clicked2
    global drop_time
    global time_label
    global update_button
    if is_on:
        on_button.config(image=off)
        is_on = False
        number_entry.destroy()
        number_label.destroy()
        update_button.destroy()
        time_label.destroy()
        drop_time.destroy()
        mins_entry.destroy()
        hrs_entry.destroy()
    else:
        number_entry = Entry(canvas_settings, font=('Arial', 15), width=13)
        number_label = Label(canvas_settings, text="Enter phone number:", bg="white", font=('Arial', 15))
        time_label = Label(canvas_settings, text="Add reminder")
        hrs_entry = Entry(canvas_settings, width=3, font=('Arial', 15))
        mins_entry = Entry(canvas_settings, width=3, font=('Arial', 15))
        time_options = ['am', 'pm']
        clicked2 = StringVar()
        clicked2.set("am")
        drop_time = OptionMenu(canvas_settings, clicked2, *time_options)
        time_label = Label(canvas_settings, text="Enter a time:", bg='white', font=('Arial', 15))
        update_button = Button(canvas_settings, text="Update Settings", bg="#76b5a5", font=('Arial', 15, 'bold'),
                               command=msg_send_time, activebackground="#76b5a5")

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


def list_badges():
    global list_of_badges
    for badge in list_of_badges:
        badge.destroy()
    badges_label = Label(stats, text="Achievements", bg="white", font=('Arial', 16, 'bold'))
    list_of_badges.append(badges_label)
    badges_label.place(x=0,y=200)

    if num_bottles >= 1:
        bottle_1 = Image.open("badge_1.png")
    else:
        bottle_1 = Image.open("badge_1_gray.png")
    bottle_1 = bottle_1.resize((100, 100), Resampling.LANCZOS)
    bottle_1 = ImageTk.PhotoImage(bottle_1)
    bottle_1_label = Label(stats, image=bottle_1, bg="white")
    bottle_1_label.image = bottle_1
    bottle_1_label.place(x=15,y=245)
    label_image.append(bottle_1_label)

    if num_bottles >= 10:
        bottle_10 = Image.open("badge_10.png")
    else:
        bottle_10 = Image.open("badge_10_gray.png")
    bottle_10 = bottle_10.resize((105, 105), Resampling.LANCZOS)
    bottle_10 = ImageTk.PhotoImage(bottle_10)
    bottle_10_label = Label(stats, image=bottle_10, bg="white")
    bottle_10_label.image = bottle_10
    bottle_10_label.place(x=165,y=245)
    label_image.append(bottle_10_label)

    if num_bottles >= 50:
        bottle_50 = Image.open("badge_50.png")
    else:
        bottle_50 = Image.open("badge_50_gray.png")
    bottle_50 = bottle_50.resize((105, 105), Resampling.LANCZOS)
    bottle_50 = ImageTk.PhotoImage(bottle_50)
    bottle_50_label = Label(stats, image=bottle_50, bg="white")
    bottle_50_label.image = bottle_50
    bottle_50_label.place(x=310,y=245)
    label_image.append(bottle_50_label)

    if num_bottles >= 100:
        bottle_100 = Image.open("badge_100.png")
    else:
        bottle_100 = Image.open("badge_100_gray.png")
    bottle_100 = bottle_100.resize((110, 110), Resampling.LANCZOS)
    bottle_100 = ImageTk.PhotoImage(bottle_100)
    bottle_100_label = Label(stats, image=bottle_100, bg="white")
    bottle_100_label.image = bottle_100
    bottle_100_label.place(x=10,y=370)
    label_image.append(bottle_100_label)

    if num_bottles >= 24:
        one_pound_plastic = Image.open("badge_1_pound.png")
    else:
        one_pound_plastic = Image.open("badge_1_pound_gray.png")
    one_pound_plastic = one_pound_plastic.resize((105, 105), Resampling.LANCZOS)
    one_pound_plastic = ImageTk.PhotoImage(one_pound_plastic)
    one_pound_plastic_label = Label(stats, image=one_pound_plastic, bg="white")
    one_pound_plastic_label.image = one_pound_plastic
    one_pound_plastic_label.place(x=165,y=375)
    label_image.append(one_pound_plastic_label)

    if num_bottles >= 120:
        five_pounds_plastic = Image.open("badge_5_pounds.png")
    else:
        five_pounds_plastic = Image.open("badge_5_pounds_gray.png")
    five_pounds_plastic = five_pounds_plastic.resize((100, 110), Resampling.LANCZOS)
    five_pounds_plastic = ImageTk.PhotoImage(five_pounds_plastic)
    five_pounds_plastic_label = Label(stats, image=five_pounds_plastic, bg="white")
    five_pounds_plastic_label.image = five_pounds_plastic
    five_pounds_plastic_label.place(x=310,y=370)
    label_image.append(five_pounds_plastic_label)


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

image_settings=image_settings.resize((80, 75))
# Convert the image in TkImage
image_settings=ImageTk.PhotoImage(image_settings)
settings_btn = Button(root, image=image_settings, bg="#76b5a5", command=change_to_settings, width=150, activebackground="#76b5a5")
settings_btn.place(x=290, y=520)

root.mainloop()
