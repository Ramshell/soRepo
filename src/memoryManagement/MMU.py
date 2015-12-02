class MMU:
    '''
    @summary: it manages the paging
    '''


    def __init__(self, frameSize,ram):
        self.frameSize = frameSize
        self.ram = ram
        self.pages = [True] * (self.ram.size / frameSize)
        
        
    def getMemoryScope(self,program):
        self.framesNeeded = program.size() / self.frameSize
        self.framesPerDataNeeded = program.variableSize / self.frameSize
        instructionPages = []
        dataPages = []
        for i in xrange(len(self.pages)):
            if self.framesNeeded < 0:
                break
            if self.pages[i]:
                instructionPages.append(i)
                self.pages[i] = False
                self.framesNeeded = self.framesNeeded-1
        for i in xrange(len(self.pages)):
            if self.framesPerDataNeeded < 0:
                break
            if self.pages[i]:
                dataPages.append(i)
                self.pages[i] = False
                self.framesPerDataNeeded = self.framesPerDataNeeded-1
        return Scope(instructionPages,dataPages)
    
    def fromPageToAbsolutePosition(self,pageNumber):
        return (pageNumber)*self.frameSize
                
    def getFrameSize(self):
        return self.frameSize
    
    def clean(self,pcb):
        for page in pcb.getPages():
            self.pages[page] = True
            
            
class Scope():
    
    def __init__(self,listInstructionPages,listDataPages):
        self.listInstructionPages = listInstructionPages
        self.listDataPages = listDataPages
        
        
    def getListDataPages(self):
        return self.listDataPages
    
    def getListInstructionPages(self):
        return self.listInstructionPages
        
        
    
        
        