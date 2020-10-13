import serial
from pynput.keyboard import Listener, Key
import datetime

import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title('test_loop')
root.geometry('300x50')
root.configure(background='ivory3')
T = tk.Text(root, height=2, width=30)
T.grid(column=0, row=1, sticky='nsew')
T.config(background='light grey', foreground='black', font='arial 20 bold', wrap='word', relief='sunken', bd=5)

def update_text():
    arduino = serial.Serial('COM3',9600)
    arduino.timeout = 2
    line = arduino.readline().decode("ASCII").rstrip("\r\n")
    T.delete("1.0", "end")  # if you want to remove the old data
    T.insert(tk.END,line)
    root.after(2000, update_text)

root.after(2000, update_text)
root.mainloop()
