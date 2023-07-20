import tkinter as tk
from tkinter import *
import json

def view_log():
    root = tk.Tk()
    root.geometry("500x400")
    root.title("Keylogger Log Viewer")

    # Read the JSON file
    with open('logs.json') as file:
        data = json.load(file)

    # Create a text area to display the log
    log_text = Text(root, height=20, width=60)
    log_text.pack(pady=10)

    # Insert the log data into the text area
    for entry in data:
        for key, value in entry.items():
            log_text.insert(END, f"{key}: {value}\n")

    root.mainloop()

# Call the JSON viewer function
view_log()
