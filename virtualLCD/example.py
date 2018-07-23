#!/usr/bin/python3
# Example using virtualLCD by 2BRobots to show a simulation of a classic
# LCD displayed on screen. Code in writen in Pyhton 3, tkinter module required.

import virtualLCD as display2BR
import time

LCD = display2BR.virtualLCD(20,4) #declare object and begin LCD with desired size

#Please note that only basic functions are available at the moment
#just as shown here in the main function.
#You can't send '\n' in the text for new line, it will be ignored
#instead use "set_cursor". If the text if bigger than the available cols
#it will be displayed automatically at the next available row.
#Any text longer than the LCD available space will be discarted.

def main():
    LCD.message("Hello world!!!")
    time.sleep(1)
    LCD.set_cursor(0,1)
    LCD.message("This LCD is working")
    time.sleep(0.25)
    LCD.set_cursor(5,2)
    LCD.message("congrats :)")
    time.sleep(3)
    LCD.set_cursor(17,3)
    LCD.message("bye")
    time.sleep(1)
    LCD.clear()
    time.sleep(1)


if __name__ == '__main__':
    while(1):
        main() 
