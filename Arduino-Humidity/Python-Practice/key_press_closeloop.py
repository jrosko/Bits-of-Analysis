import serial
import time
from pynput.keyboard import Listener, Key
import datetime

# x = datetime.datetime.now()
#
# print(x.strftime("%X"))

def on_press(key):
    pass

def on_release(key):
    if key == Key.shift:
        print('Exiting Program')
        return False

arduino = serial.Serial('COM3',9600)
arduino.timeout = 2

with Listener(on_press=on_press, on_release = on_release) as listener:
    #listener.join() # This would join the main thread. If this is on, the code will just wait for a key and then break
    while True:
        time.sleep(1)
        if listener.running == False:
            break
        else:
            line = arduino.readline().decode("ASCII").rstrip("\r\n")
            if len(line)>0:
                print(line)
