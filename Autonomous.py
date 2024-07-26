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
    gpio.setup(12, gpio.OUT)
    gpio.setup(16, gpio.IN)

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
 


def distance(mesure='cm'):
    init()
    gpio.output(12, False)
    while gpio.input(16) == 0:
        nosig = time.time()

    while gpio.input(16) == 1:
        sig = time.time()   #sig = signale / nosig = no signale

    tl = sig - nosig # tl= time long

    if measure == 'cm':
        distance = tl / 0.000058
    elif mesaure == 'in':
        distance = tl / 0.000148
    else:
        print('improper coice of measurement : in or cm')
        distance = None
    gpio.cleanup()
    return distance

  '''
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

    curDis = distance('cm')
    print('curDis is ', curDis)

    if curDis < 20:
        init()
        reverse(2)
  '''


    

command = tk.Tk()
command.bind('keyPress', key_input)
command.mainloop()




print(distance('cm'))





def automomy():
    tf = 0.030
    x = random.randrange(0,4)
