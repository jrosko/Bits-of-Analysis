import serial
from pynput.keyboard import Listener, Key
import datetime

import tkinter as tk
from tkinter import scrolledtext
import time
import queue
import threading



root = tk.Tk()
root.title('test_loop')
root.geometry('300x50')
root.configure(background='ivory3')
T = tk.Text(root, height=2, width=30)
T.grid(column=0, row=1, sticky='nsew')
T.config(background='light grey', foreground='black', font='arial 20 bold', wrap='word', relief='sunken', bd=5)

q = queue.Queue()

def get_data(port, baud, delay):
    arduino = serial.Serial(port, baud)
    arduino.timeout = 2
    while True:
        line = arduino.readline().decode("ASCII").rstrip("\r\n")
        q.put(line)
        time.sleep(delay)

def print_data(q):
    while True:
        time.sleep(5)
        if q.empty() == False:
            item = q.get()
            print(item)
            q.task_done()

data_thread = threading.Thread(target = get_data, args = ['COM3', 9600, 5])
print_thread = threading.Thread(target = print_data, args = [q])
data_thread.start()
print_thread.start()


#
#
# def update_text():
#     arduino = serial.Serial('COM3',9600)
#     arduino.timeout = 2
#     line = arduino.readline().decode("ASCII").rstrip("\r\n")
#     T.delete("1.0", "end")  # if you want to remove the old data
#     T.insert(tk.END,line)
#     root.after(2000, update_text)
#
# root.after(2000, update_text)
# root.mainloop()
