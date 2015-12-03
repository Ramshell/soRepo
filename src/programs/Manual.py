
class Manual(object):

    def __init__(self, name, description=None, arguments=None):
        self.name = name
        self.description = description
        self.arguments = arguments
        
    def setDescription(self, description):
        self.description = description
        
    def setArguments(self, arguments):
        self.arguments = arguments
    
    def printManual(self, impressor = None):
        to_print_manual = "Name: " + self.name + " \n"
        if self.description != None:
            to_print_manual = to_print_manual + "Description: " + self.name + " was created to " + self.description + " \n"
        if self.arguments != None:
            to_print_manual = to_print_manual + "Arguments: " + " \n"
            for argument in self.arguments:
                to_print_manual = to_print_manual + argument
            
        return to_print_manual
