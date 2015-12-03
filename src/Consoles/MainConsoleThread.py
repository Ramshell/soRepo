from threading import *
from Tkinter import *
from MainConsole import MainConsole
import codecs
import os
'''
Main Thread that starts the console application

@author: Nicolas Leutwyler
@author: Lucas Sandoval
@author: Jesus Laime
'''

class MainConsoleThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.con = None
        self.start()
    
    def write(self,message):
        self.con.write(message)
        
    def writeCpuLog(self,message):
        self.con.writeCpuLog(message)
        
    def writeScreenLog(self,message):
        self.con.writeScreenLog(message)
    
    def writePrinterLog(self,message):
        self.con.writePrinterLog(message)
        
    def run(self):
        self.con = MainConsole()
        self.con.startUp()

if __name__ == '__main__':
    thread = MainConsoleThread()