import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Four Buttons")

# Set the window size
root.geometry("432x768")
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

# Create the buttons
button1 = tk.Button(button_frame, text="Button 1")
button1.pack(side=tk.LEFT, padx=5)

button2 = tk.Button(button_frame, text="Button 2")
button2.pack(side=tk.LEFT, padx=5)

button3 = tk.Button(button_frame, text="Button 3")
button3.pack(side=tk.LEFT, padx=5)

button4 = tk.Button(button_frame, text="Button 4")
button4.pack(side=tk.LEFT, padx=5)

root.mainloop()