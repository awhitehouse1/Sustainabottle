import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Main Menu")

# Set the window size
root.geometry("432x600")
root.resizable("False", "False")

main_frame = tk.Frame(root)
stats_frame = tk.Frame(root)
settings_frame = tk.Frame(root)


def change_to_main():
    main_frame.pack(fill='both', expand=1)
    settings_frame.pack_forget()
    stats_frame.pack_forget()


def change_to_stats():
    stats_frame.pack(fill='both', expand=1)
    main_frame.pack_forget()
    settings_frame.pack_forget()

def change_to_settings():
    settings_frame.pack(fill='both', expand=1)
    main_frame.pack_forget()
    stats_frame.pack_forget()


main_btn = tk.Button(root, text="Main", width=20, height=7, command=change_to_main())
main_btn.pack(side=tk.LEFT)

stats_btn = tk.Button(root, text="Stats", width=20, height=7, command=change_to_stats())
stats_btn.pack(side=tk.LEFT)

settings_btn = tk.Button(root, text="Settings", width=20, height=7, command=change_to_settings())
settings_btn.pack(side=tk.LEFT)



root.mainloop()
