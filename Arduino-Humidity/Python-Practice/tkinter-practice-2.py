import serial
import tkinter as tk
import time
import queue
import threading
import random as rand

class GuiPart:
    measurement = ''

    def __init__(self, master, queue, endCommand):
        self.queue = queue
        self.master = master
        #master.geometry('300x50')
        exit_button = tk.Button(self.master, text='Quit', command=endCommand)
        self.text = tk.Text(self.master, height=3, width=40)
        self.text.pack(side = 'bottom')
        exit_button.pack(side='left')

    def processIncoming(self):
        while self.queue.qsize()>0:
            try:
                self.measurement = self.queue.get(0)
                self.text.delete("1.0", "end")  # if you want to remove the old data
                self.text.insert(tk.END,self.measurement)
            except queue.empty:
                pass

class ThreadedClient:
    arduino = serial.Serial('COM3', 9600)
    arduino.timeout = 2
    def __init__(self, master):
        self.master = master
        self.queue = queue.Queue()
        self.gui = GuiPart(master, self.queue, self.endApplication)
        self.running = 1
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()
        self.periodicCall()

    def periodicCall(self):
        self.gui.processIncoming()
        if not self.running:
            import sys
            sys.exit(1)
        self.master.after(5000, self.periodicCall)

    def workerThread1(self):
        while self.running:
            time.sleep(2)
            try:
                line = self.arduino.readline().decode("ASCII").rstrip("\r\n")
                if len(line)>0:
                    self.queue.put(line)
            except:
                pass

    def endApplication(self):
        self.running = 0

master = tk.Tk()
client = ThreadedClient(master)
master.mainloop()
