import RPi.GPIO as gpio 
import time
import sys
import tkinter as tk


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)


def forward(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.outpt(15, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def Turn_left(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


def Turn_right(tf):  #tf= time frem 
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


def Pivot_left(tf):
    gpio.outpit(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()



def Pivot_right(tf):
    gpio.outpit(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()
 


def key_input(event):
    init()
    print ('key', event.char)
    key_press = event.char
    sleep_time = 0.030
 
    if key_press.lower() == 'w':
         forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    if key_press.lower() == 'a':
         Turn_left(sleep_time)
    elif key_press.lower() == 'd':
        Turn_right(sleep_time)
    if key_press.lower() == 'q':
         Pivot_left(sleep_time)
    elif key_press.lower() == 'e':
        Pivot_right(sleep_time)
    else:
        pass
    

command = tk.Tk()
command.bind('keyPress', key_input)
command.mainloop()



