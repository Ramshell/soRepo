from Tkinter import *
import codecs
import os

class MainConsole(Frame):

    def __init__(self):
        self.mainWindow = Tk()
        self.mainMenu = Menu(self.mainWindow)
        self.mainWindow.config(menu=self.mainMenu)
        self.cpuWindow = None
        self.screenWindow = None
        self.printerWindow = None
        self.textViewCpu = None
        self.textViewScreen = None
        self.textViewPrinter = None
        self.createContents()
        
    def startUp(self):
        self.mainWindow.mainloop()

    def createContents(self):
        self.mainWindow.config(bg="black")
        self.mainWindow.geometry("700x500")
        text = Text(self.mainWindow)
        text.pack()
        text.config(bg="black",fg="white")
        self.mainWindow.resizable(0,0)
        self.createTopLevelWindows()
        self.createMenues()
        
    def createTopLevelWindows(self):
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
        self.newWindow = Toplevel(self.mainWindow)
        self.newWindow.title(name+" Console")
        self.newWindow.config(bg="black")
        self.newWindow.geometry("500x350")
        return self.newWindow
    
    def createMenues(self):
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
        aMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label=name, menu=aMenu)
        aMenu.add_command(label="Open Window",command= lambda1)
        aMenu.add_command(label="Close Window",command= lambda2)
        
    def openCpu(self):
        enlace = "../log/cpu_log"
        self.cpuWindow.deiconify()
        #if os.path.exists(enlace):
        file = open(enlace, "r")
        data = file.read()
        self.textViewCpu.insert(END,data)
        file.close()
        
    def closeCpu(self):
        self.textViewCpu.delete("1.0", END)
        self.cpuWindow.withdraw()
        
    def openPrinter(self):
        enlace = "../log/printer_log"
        self.printerWindow.deiconify()
        if os.path.exists(enlace):
            file = open(enlace, "r")
            data = file.read()
            self.textViewPrinter.insert(END,data)
            file.close()
        
    def closePrinter(self):
        self.textViewPrinter.delete("1.0", END)
        self.printerWindow.withdraw()
        
    def openScreen(self):
        enlace = "../log/screen_log"
        self.screenWindow.deiconify()
        if os.path.exists(enlace):
            file = open(enlace, "r")
            data = file.read()
            self.textViewScreen.insert(END,data)
            file.close()
        
    def closeScreen(self):
        self.textViewScreen.delete("1.0", END)
        self.screenWindow.withdraw()
        
    