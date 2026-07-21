#!/usr/bin/env python3
########################################################################
# Filename    : I2CLCD1602.py
# Description : Use the LCD display data
# Author      : freenove
# modification: 2023/05/15
########################################################################
import smbus
from time import sleep, strftime
from datetime import datetime
from LCD1602 import CharLCD1602

lcd1602 = CharLCD1602()


def loop():
    lcd1602.init_lcd()
    print('LCD1602 is working ...')
    count = 0
    while (True):
        lcd1602.clear()
        lcd1602.write(0, 0, 'Hello, Oliver!')
        lcd1602.write(0, 1, 'Count: ' + str(count))   # display the time
        sleep(1)
        count += 1


def destroy():
    lcd1602.clear()


if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
