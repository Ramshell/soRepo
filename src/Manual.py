
class Manual(object):

    def __init__(self, name, description=None, arguments=None):
        self.name = name
        self.description = description
        self.arguments = arguments
        
    def setDescription(self, description):
        self.description = description
        
    def setArguments(self, arguments):
        self.arguments = arguments
    
    def printManual(self):
        print "Name: ", self.name
        if self.description != None:
            print "Description: ", self.name, "was created to ", self.description
        if self.arguments != None:
            print "Arguments: "
            for argument in self.arguments:
                print "- ", argument
            
        
