'''
Logs every print of system, on a file called "fileDir"

@author: Nicolas Leutwyler
@author: Lucas Sandoval
@author: Jesus Laime
'''
from datetime import datetime


class FileLogger:
    
    def __init__(self, fileDir,mainConsole):
        '''
        Constructor of the file logger.
        
        @param fileDir: Directory to create or update logs 
        ''' 
        self.dir = fileDir
    
    def log(self, txt):
        '''
        Logs into his correspond file directory, the message send with a format that shows time and date
        
        @param txt: Message to log
        '''
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.file = open(self.dir, "a")
        self.message = self.date + "   -   " + txt + "\n"
        self.file.write(self.message)
        self.logOnConsole(self.message)
        self.file.close()
        
    def logOnConsole(self,message):
        pass

class ScreenFileLogger(FileLogger):
    '''
    classdocs
    '''


    def __init__(self, fileDir,mainConsole):
        '''
        Constructor
        '''
        FileLogger.__init__(self, fileDir, mainConsole)
        self.consoleToLog = mainConsole
        
    def logOnConsole(self, message):
        FileLogger.logOnConsole(self, message)
        self.consoleToLog.writeScreenLog(message)
        
class CpuFileLogger(FileLogger):
    '''
    classdocs
    '''


    def __init__(self, fileDir,mainConsole):
        '''
        Constructor
        '''
        FileLogger.__init__(self, fileDir, mainConsole)
        self.consoleToLog = mainConsole
        
    def logOnConsole(self, message):
        FileLogger.logOnConsole(self, message)
        self.consoleToLog.writeCpuLog(message)
        
        
class PrinterFileLogger(FileLogger):
    '''
    classdocs
    '''


    def __init__(self, fileDir,mainConsole):
        '''
        Constructor
        '''
        FileLogger.__init__(self, fileDir, mainConsole)
        self.consoleToLog = mainConsole
        
    def logOnConsole(self, message):
        FileLogger.logOnConsole(self, message)
        self.consoleToLog.writePrinterLog(message)