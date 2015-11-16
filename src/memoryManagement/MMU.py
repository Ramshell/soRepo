class MMU(object):
    '''
    @summary: it manages the paging
    '''


    def __init__(self, frameSize,ram):
        self.frameSize = frameSize
        self.ram = ram
        self.pages[self.ram.size / frameSize] * True
        
        
    def memoryScopeFor(self,program):
        self.framesNeeded = (program.size / self.frameSize) +1
        res = []
        for i in xrange(self.pages.size):
            if self.pages[i]:
                res.append(i*self.frameSize)
                self.pages[i] = False
                self.framesNeeded = self.framesNeeded-1
            if self.framesNeeded == 0:
                break
        return res
                
        