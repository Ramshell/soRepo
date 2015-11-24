from Exceptions import *

class InvalidProgramException(Exception):
    '''
    classdocs
    '''


    def __init__(self, params):
        Exception.__init__(self,params)
        
        