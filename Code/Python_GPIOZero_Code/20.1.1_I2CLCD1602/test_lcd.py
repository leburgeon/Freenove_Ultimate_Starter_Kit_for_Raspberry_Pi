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


def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def loop():
    lcd1602.init_lcd()
    print('LCD1602 is working ...')
    while (True):
        time = get_time()
        old_time = ''
        if time != old_time:
            old_time = time
            lcd1602.write(0, 0, 'Hello, Lewis!')
            lcd1602.write(0, 1, 'Time: ' + time)   # display the time


def destroy():
    lcd1602.clear()


if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
