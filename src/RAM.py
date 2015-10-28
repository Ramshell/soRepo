

class RAM:



    def __init__(self, size):
        self.content = []
        self.size = size
        self.libre = 0
        
    def getMemoryScope(self,size):
        return len(self.content)
    
    def getDir(self, i):
        return self.content[i]
    
    def putDir(self, i, inst):
        self.content.append(inst)
        self.libre = self.libre + 1 
    
    def delete(self):
        pass

    def clean(self,pcb):
        pass