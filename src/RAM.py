

class RAM:



    def __init__(self, size):
        self.content = [None] * size
        self.size = size
        self.libre = 0
        
    def getMemoryScope(self, size):
        return self.libre
    
    def getDir(self, i):
        return self.content[i]
    
    def putDir(self, i, inst):
        self.content[i] = inst
        self.libre = self.libre + 1
    
    def reserve(self, number):
        absolutePosition = self.libre
        self.libre = self.libre + number
        return absolutePosition
    
    def delete(self):
        pass

    def clean(self, pcb):
        pass
