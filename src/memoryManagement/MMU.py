class MMU(object):
    '''
    @summary: it manages the paging
    '''


    def __init__(self, frameSize,ram):
        self.frameSize = frameSize
        self.ram = ram
        self.pages = [True] * (self.ram.size / frameSize)
        
        
    def getMemoryScope(self,program):
        self.framesNeeded = ((program.size() + program.variableSize) / self.frameSize)
        res = []
        for i in xrange(len(self.pages)):
            if self.pages[i]:
                res.append(i)
                self.pages[i] = False
                self.framesNeeded = self.framesNeeded-1
            if self.framesNeeded <= 0:
                break
        return res
    
    def fromPageToAbsolutePosition(self,pageNumber):
        return (pageNumber)*self.frameSize
                
    def getFrameSize(self):
        return self.frameSize
    
    def clean(self,pcb):
        for page in pcb.getPages():
            self.pages[page] = True
        
        