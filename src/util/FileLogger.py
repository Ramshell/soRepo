'''
Logs every print of system, on a file called "fileDir"

@author: Sandoval Lucas
@author: Leutwyler Nicolas
@author: Laime Jesus 
'''

from datetime import datetime


class FileLogger:
    
    def __init__(self, fileDir):
        self.dir = fileDir
    
    def log(self, txt):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.file = open(self.dir, "a")
        self.message = "// " + self.date + " - " + txt + " //" + "\n"
        self.file.write(self.message)
        self.file.close()
