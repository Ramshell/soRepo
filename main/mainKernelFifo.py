from programs.Manual import Manual
from factories.OperativeSystemFactory import OperativeSystemFactory
from storage.RAM import RAM
from scheduler.Scheduler import Scheduler
from Consoles.Shell import Shell
from factories.discFactory import diskFactory
from Consoles.MainConsoleThread import MainConsoleThread
from util.FileLogger import ScreenFileLogger, PrinterFileLogger


if __name__ == '__main__':
    diskFc = diskFactory()
    disk = diskFc.basicHDD()
    mainConsole = MainConsoleThread()
    osFc = OperativeSystemFactory(disk, RAM(65535),4,mainConsole)
    loggerScreen = ScreenFileLogger("../log/screen_log",mainConsole)
    loggerPrinter = PrinterFileLogger("../log/printer_log",mainConsole)
    os = osFc.fifo()
    os.installNewDevice("printer",loggerScreen)
    os.installNewDevice("screen",loggerPrinter)
    os.startUp()
    shell = Shell(mainConsole,os)
    shell.start()
