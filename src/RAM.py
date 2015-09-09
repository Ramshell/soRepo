

class RAM:



    def __init__(self, size):
        self.content = []
        self.size = size
        
    def getMemoryScope(self):
        return len(self.content) + 1
    
    def getDir(self, i):
        return self.content[i]
    
    def putDir(self, i, inst):
        self.content[i] = inst
    
    
