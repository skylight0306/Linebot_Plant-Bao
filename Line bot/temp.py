# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
from pyfirmata import Arduino, util
from time import sleep
import serial
"""


#s = serial.Serial("com3",9600)

from pyfirmata import Arduino, util
from pyfirmata.util import Iterator
from time import sleep

# Setting up the Arduino board
port = 'COM3'
board = Arduino(port)
# Need to give some time to pyFirmata and Arduino to synchronize
sleep(1)

# Start Iterator to avoid serial overflow
import pyfirmata 
it = util.Iterator(board)
it.start()
#board.analog[0].mode = pyfirmata.INPUT
#board.analog[1].mode = pyfirmata.INPUT
# Assign a role and variable to analog pin 0
#type(d8)

a0 = board.get_pin('a:0:i')
a1 = board.get_pin('a:1:i')
a2 = board.get_pin('a:2:i')
#d8 = board.get_pin('d:8:i')
# Running loop for ever

arr = []

try:
    while True:
        sleep(1)
        # Reading value on port a0
        #print(board.analog[0].read())
        #print(board.analog[1].read())
        p = a0.read()
        
        pp = a1.read()
        
        ppp = a2.read()
        
        if p and pp and ppp :
            arr.append(p)
            arr.append(pp)
            arr.append(ppp)
            break ;
        
        """
        p = a0.read()
        print(p)
        
        
        D8 = d8.read()
        print(D8)
        """
    f1 = open('/Line bot/plant_inf.txt','w',encoding="utf-8")
    f1.write(p)
    f1.write(pp)
    f1.write(ppp)
    print(arr)
except KeyboardInterrupt:
    board.exit()

"""
PIN = 8

num = board.digital[PIN].read()

#uno.exit()"""