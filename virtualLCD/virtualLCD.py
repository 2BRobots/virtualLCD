#!/usr/bin/python3

# Copyright (c) 2018 2BRobots
# Author: dannimakes
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from tkinter import *

class virtualLCD(object):

    def __init__(self,cols,rows):
        self.root = Tk()
        self.root.title("virtualLCD")
        self.root.geometry("+500+100")
        self.buffer = ""
        self.buffer = self.buffer.ljust(cols*rows)
        self.labelfont = ('Courier', 24, 'bold')
        self.widget = Label(self.root, text=self.buffer, height=rows, width=cols, anchor=NW, justify=LEFT)
        self.widget.config(bg='yellow', fg='black') #here you can change the background and text color of the LCD 
        self.widget.config(font=self.labelfont)            
        self.widget.pack(expand=YES, fill=BOTH)
        self.root.update()
        self.cols = cols
        self.rows = rows
        self.clear()
                
    def clear(self):
        self.set_cursor(0,0)
        self.buffer = ""
        self.buffer = self.buffer.ljust(self.cols*self.rows)
        self.widget.config(text=self.buffer)
        self.widget.pack(expand=YES, fill=BOTH)
        self.root.update()
       
    def message(self,data):
        data = data.replace('\n','')
        self.buffer = self.buffer.replace('\n','')
        data = self.buffer[:self.cursor] + data + self.buffer[(self.cursor+len(data)):]
        data = data[:(self.cols*self.rows)]
        data = '\n'.join([data[i:i + self.cols] for i in range(0, len(data), self.cols)])
        self.widget.config(text=data)
        self.buffer = data
        self.root.update()

    def set_cursor(self,x,y):
        self.cursor = ((y*self.cols)+x)
