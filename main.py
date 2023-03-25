# Import the required libraries
from tkinter import *
from tkinter import font

# Create an instance of tkinter frame or window
root = Tk()

# Set the size of the window
root.geometry("432x600")
root.resizable("False", "False")

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
label1 = Label(main_menu, text="in main", foreground="green3")
label1.place(x=-5,y=0)

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
