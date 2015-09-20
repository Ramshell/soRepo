from abc import abstractmethod


class Instruction:
    


    def __init__(self, valor):
        self.value = valor
        
        
    def run(self):
        print(self.value)    
    
    @abstractmethod
    def isIO(self):
        pass
