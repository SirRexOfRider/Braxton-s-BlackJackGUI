class Card:
    
    #DA
    __value = -1
    __suite = ""
    __type = ""
    
    
    #Init
    def __init__(self, value, suite, type):
        self.set_value(value)
        self.set_suite(suite)
        self.set_type(type)
        
        
    #Helpers
    
    #Getters
    def get_value(self):
        return self.__value
    
    def get_suite(self):
        return self.__suite
    
    def get_type(self):
        return self.__type
    
    
    #Setters
    def set_value(self, val):
        self.__value = val
        
    def set_suite(self, s):
        self.__suite = s
        
    def set_type(self, t):
        self.__type = t
    
    #To string
    def __str__(self):
        return "CARD: \n\tValue: " + str(self.get_value()) +  "\n\tType: " + str(self.get_type()) + "\n\tSuite: " + str(self.get_suite()) 
        
    
    