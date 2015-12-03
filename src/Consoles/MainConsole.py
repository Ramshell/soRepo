from Tkinter import *
from PIL import Image,ImageTk
import time
import codecs
import os

'''
@summary: Console Application for the NaNDoS Operative System

'''
class MainConsole(Frame):

    def __init__(self):
        '''
        Constructor of the app
        '''
        self.mainWindow = Tk() #Main Window
        self.mainMenu = Menu(self.mainWindow) #Main Menu
        self.mainWindow.config(menu=self.mainMenu)
        self.logoWindow = None #Logo Window
        #These are the secondary level windows
        self.cpuWindow = None
        self.screenWindow = None
        self.printerWindow = None
        #These are the text view associated to the secondary level windows
        self.textViewCpu = None
        self.textViewScreen = None
        self.textViewPrinter = None
        self.mainText = None #Main text view
        global photo #Global Image
        self.label1 = None
        self.createContents()
        
    def startUp(self):    
        '''
        Starts the app
        '''    
        self.mainWindow.mainloop()

    def createContents(self):
        '''
        Method that builds the entire application
        '''
        self.mainWindow.config(bg="black")
        self.mainWindow.geometry("700x500")
        self.mainText = Text(self.mainWindow)
        self.mainText.config(bg="black",fg="white",height="500",width="700")
        self.mainText.pack()
        self.mainWindow.resizable(0,0)
        self.createTopLevelWindows()
        self.createMenues()
        self.createFinalWindow()
        self.defineExitProtocol()
        
    def createTopLevelWindows(self):
        '''
        Creates all the secondary level windows
        '''
        self.cpuWindow = self.createTopLevelWindow("cpu")
        self.cpuWindow.resizable(0,0)
        self.textViewCpu = Text(self.cpuWindow)
        self.textViewCpu.config(bg="black",fg="white")
        self.textViewCpu.pack()
        self.cpuWindow.withdraw()
        self.printerWindow = self.createTopLevelWindow("printer")
        self.printerWindow.resizable(0,0)
        self.textViewPrinter = Text(self.printerWindow)
        self.textViewPrinter.config(bg="black",fg="white")
        self.textViewPrinter.pack()
        self.printerWindow.withdraw()
        self.screenWindow = self.createTopLevelWindow("screen")
        self.screenWindow.resizable(0,0)
        self.textViewScreen = Text(self.screenWindow)
        self.textViewScreen.config(bg="black",fg="white")
        self.textViewScreen.pack()
        self.screenWindow.withdraw()
        
    def createTopLevelWindow(self,name):
        '''
        Create a single secondary level window
        '''
        self.newWindow = Toplevel(self.mainWindow)
        self.newWindow.title(name+" Console")
        self.newWindow.config(bg="black")
        self.newWindow.geometry("500x350")
        return self.newWindow
    
    def createMenues(self):
        '''
        Creates all the menus
        '''
        lambda1 = lambda: self.openCpu()
        lambda2 = lambda: self.closeCpu()
        self.createComponentMenu("CPU Console" ,lambda1 ,lambda2)
        lambda1 = lambda: self.openScreen()
        lambda2 = lambda: self.closeScreen()
        self.createComponentMenu("Screen Console",lambda1 ,lambda2)
        lambda1 = lambda: self.openPrinter()
        lambda2 = lambda: self.closePrinter()
        self.createComponentMenu("Printer Console",lambda1 ,lambda2)
        
    def createComponentMenu(self,name,lambda1,lambda2):
        '''
        Create the components of a specific menu
        '''
        aMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label=name, menu=aMenu)
        aMenu.add_command(label="Open Window",command= lambda1)
        aMenu.add_command(label="Close Window",command= lambda2)
        
    def createFinalWindow(self):
        '''
        Create the logo window
        '''
        self.logoWindow = Toplevel(self.mainWindow)
        self.logoWindow.geometry("380x240")
        self.logoWindow.configure(background='black')
        photo = PhotoImage( file="../resources/images/startImage.gif")
        self.canvas = Canvas(self.logoWindow)
        self.canvas.pack()
        self.canvas.create_image(190,150,image=photo)
        self.canvas.image = photo
        #self.exitWindow.withdraw()
        
    def defineExitProtocol(self):
        '''
        Defines bindings for the app
        '''
        self.mainWindow.bind('<Escape>', lambda e: self.showLogo())
        
    def openCpu(self):
        '''
        Opens the cpu console
        '''
        enlace = "../log/cpu_log"
        self.cpuWindow.deiconify()
        if os.path.exists(enlace):
            file = open(enlace, "r")
            data = file.read()
            self.textViewCpu.insert(END,data)
            file.close()
        
    def closeCpu(self):
        '''
        Closes the cpu console
        '''
        self.textViewCpu.delete("1.0", END)
        self.cpuWindow.withdraw()
        
    def openPrinter(self):
        '''
        Opens the printer console
        '''
        enlace = "../log/printer_log"
        self.printerWindow.deiconify()
        if os.path.exists(enlace):
            file = open(enlace, "r")
            data = file.read()
            self.textViewPrinter.insert(END,data)
            file.close()
        
    def closePrinter(self):
        '''
        Closes the printer console
        '''
        self.textViewPrinter.delete("1.0", END)
        self.printerWindow.withdraw()
        
    def openScreen(self):
        '''
        Opens the screen console
        '''
        enlace = "../log/screen_log"
        self.screenWindow.deiconify()
        if os.path.exists(enlace):
            file = open(enlace, "r")
            data = file.read()
            self.textViewScreen.insert(END,data)
            file.close()
        
    def closeScreen(self):
        '''
        Closes the screen console
        '''
        self.textViewScreen.delete("1.0", END)
        self.screenWindow.withdraw()
        
        
    
    
    
    
    
    ######################################################
    ######################################################
    ######################################################
    
    def write(self,message):
        '''
        Prints a message on the main window
        '''
        self.mainText.insert(END, message)
        self.mainText.see(END)
    
    def writeCpuLog(self, message):
        '''
        Print a message on the cpu console
        '''
        self.textViewCpu.insert(END, message)
        self.textViewCpu.see(END)
        
    def writeScreenLog(self, message):
        '''
        Print a message on the screen console
        '''
        self.textViewScreen.insert(END, message)
        self.textViewScreen.see(END)
        
    def writePrinterLog(self, message):
        '''
        Print a message on the printer console
        '''
        self.textViewPrinter.insert(END, message)
        self.textViewPrinter.see(END)

    def showLogo(self):
        '''
        Method that occurs when the closure of the app
        '''
        self.mainWindow.withdraw()
        time.sleep(3)
        self.exitWindow.deiconify()
        time.sleep(3)
        self.mainWindow.destroy()
        
if __name__ == '__main__':
    shell = MainConsole()
    shell.startUp()
    