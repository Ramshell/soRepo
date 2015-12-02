from Tkinter import *
import codecs
import os
from Consoles.ConsoleSecondary import ConsoleSecondary
from pango import Weight

class CpuConsole(Frame):

    def __init__(self):
        self.mainWindow = Tk()
        self.createContents()
        
        
        #self.windowForCpu = ConsoleSecondary("CONSOLE CPU" , self.mainWindow , "../log/cpu_log")
        
    def startUp(self):
        self.mainWindow.mainloop()

    def createContents(self):
        self.mainWindow.config(bg="black")
        self.mainWindow.geometry("700x500")
        text = Text(self.mainWindow)
        text.pack()
        text.config(bg="black",fg="white")
        self.mainWindow.resizable(0,0)
        self.createButtons()
        
    def createButtons(self):
        cpuButton = Button(self.mainWindow,text="Open Cpu Log")
        cpuButton.pack()#grid(row=1,column=0)
        printerButton = Button(self.mainWindow,text="Open Printer Log")
        printerButton.pack()#.grid(row=1,column=1)
        otro = Button(self.mainWindow,text="Open askjd Log")
        otro.pack()#.grid(row=1,column=2)

if __name__ == '__main__':

    
    console = CpuConsole()
    console.startUp()