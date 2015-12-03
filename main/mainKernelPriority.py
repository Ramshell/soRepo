from factories.OperativeSystemFactory import OperativeSystemFactory
from storage.RAM import RAM
from Consoles.Shell import Shell
from Consoles.MainConsoleThread import MainConsoleThread
from factories.discFactory import diskFactory
from util.FileLogger import *


if __name__ == '__main__':
    
    diskFc = diskFactory()
    disk = diskFc.basicHDD()
    ######
    mainConsole = MainConsoleThread()
    #####
    osFc = OperativeSystemFactory(disk,RAM(65535),4,mainConsole)
    os = osFc.roundRobin_withPriority(2)
    
    loggerScreen = ScreenFileLogger("../log/screen_log",mainConsole)
    loggerPrinter = PrinterFileLogger("../log/printer_log",mainConsole)
    
    os.installNewDevice("printer",loggerPrinter)
    os.installNewDevice("screen",loggerScreen)
    os.startUp()
    shell = Shell(mainConsole,os)
    shell.start()
    
    
    
