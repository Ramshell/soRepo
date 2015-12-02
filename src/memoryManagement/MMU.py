class MMU:
    '''
    @summary: it manages the paging
    @var frameSize
    @var ram: the memory RAM to make the paging
    @var pages: the free pages
    @invariant: the pages are ready to be used
    '''
    

    def __init__(self, frameSize,ram):
        '''
        @param ram: memory ram
        @param frameSize: the size of the frames
        '''
        self.frameSize = frameSize
        self.ram = ram
        self.pages = self.initializePages()
        
        
    def getMemoryScope(self,program):
        '''
        @return the Scope object the program needs
        @see: Scope
        '''
        framesNeeded = ((program.size() - 1) / self.frameSize) +1
        if program.variableSize > 0:
            framesPerDataNeeded = ((program.variableSize -1) / self.frameSize) +1
        else:
            framesPerDataNeeded = 0
        instructionPages = self.fulfilPages(framesNeeded)
        dataPages = self.fulfilPages(framesPerDataNeeded)
        return Scope(instructionPages,dataPages)
    
    def fromPageToAbsolutePosition(self,pageNumber):
        '''
        @return given a pageNumber returns the frame's first cell absolute position
        '''
        return (pageNumber) * self.frameSize
                
    def getFrameSize(self):
        return self.frameSize
    
    def clean(self,pcb):
        '''
        @return given a pcb turn its pages to be available again
        '''
        for page in pcb.getPages():
            if page.isInMemory():
                page.changeMemoryFlag()
            self.pages.append(page)
        for page in pcb.getDataPages():
            if page.isInMemory():
                page.changeMemoryFlag()
            self.pages.append(page)
            
    def getNumberOfPages(self, frameSize):
        return self.ram.size / frameSize
    
    def initializePages(self):
        res = []
        for pageNumber in xrange(self.getNumberOfPages(self.frameSize)):
            res.append(Page(pageNumber))
        return res
    
    def fulfilPages(self,framesNeeded):
        currentValue = framesNeeded
        res = []
        for page in self.pages:
            if currentValue <= 0:
                break
            res.append(page)
            self.pages.remove(page)
            currentValue = currentValue-1
            
        return res
            
            
class Scope():
    '''
    @summary: It is the abstraction of the scope needed by a program, for both instructions and data
    @var listInstructionPages
    @var listDataPages
    '''
    
    def __init__(self,listInstructionPages,listDataPages):
        self.listInstructionPages = listInstructionPages
        self.listDataPages = listDataPages
        
        
    def getListDataPages(self):
        return self.listDataPages
    
    def getListInstructionPages(self):
        return self.listInstructionPages
        
        
    
class Page():
    '''
    @summary: It represents a logic memory page with the physic memory frame associated
    '''
    
    def __init__(self,pageNumber):
        '''
        @param pageNumber: the number of the page to be bounded
        '''
        self.pageNumber = pageNumber
        self.isInMemoryFlag = False
        
    def isInMemory(self):
        '''
        @return: true if the page is in the memory yet
        '''
        return self.isInMemoryFlag
    
    def changeMemoryFlag(self):
        self.isInMemoryFlag = not self.isInMemoryFlag
        
    def getPageNumber(self):
        return self.pageNumber
        
        