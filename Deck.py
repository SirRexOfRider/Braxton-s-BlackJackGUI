from Card import Card
from random import randint



class Deck:
    
    #DA
    __deck = []
    
    #This is a special tool that will help us later :)
    #Which is why the suites don't also have/need it
    __LIST_OF_TYPES = ["Ace","Jack","Queen","King"]
    
        
    #Init
    def __init__(self, deck):
        self.set_deck(self.build_deck(deck))
    
    #helpers
    def get_value(self, val):
        temp = val
        
        if (val == 11 or val == 12 or val == 13):
            temp = 10
        elif (val == 1):
            temp = [1,11]
        
        return temp
        
        
    def get_suite(self, val):
        temp = "None"
        
        if (val == 0):
            temp = "Clubs"
        elif(val == 1):
            temp = "Spades"
        elif (val == 2):
            temp = "Hearts"
        elif (val == 3):
            temp = "Diamonds"
            
        return temp
   
 
    def get_type(self, val):
        temp = ""
        if (val == 1):
            temp = self.get_list_of_types()[0]
        elif (val == 11):
            temp = self.get_list_of_types()[1]
        elif(val == 12):
            temp = self.get_list_of_types()[2]
        elif(val == 13):
            temp = self.get_list_of_types()[3]
            
        return temp
        

    def build_deck(self,deck):
        
        #Build an empty deck

        for i in range(4):
            for j in range(13):
                deck.append(Card(self.get_value(j+1), self.get_suite(i), self.get_type(j+1)))
                
        return deck
    
    
    
    def shuffle(self):
        #Empty deck to store shuffle
        shuffled_deck = []
        
        #Empty list of used random numbers/indexes
        used_nums = []
        
        #For every card in the deck, shuffle it randomly into the shuffled deck
        for i in range(52):
            
            val = randint(0,51)

            while (val in used_nums):
                val = randint(0,51)
                
            shuffled_deck.append(self.get_deck()[val])
            used_nums.append(val)
        
        #Set the deck to the shuffled deck
        self.set_deck(shuffled_deck)
        
        
    
    def deal(self):
        temp = ""
        temp = self.get_deck()[0]
        self.get_deck().remove(self.get_deck()[0])
        return temp
        
              
    #getters
    def get_deck(self):
        return self.__deck
    
    def get_list_of_types(self):
        return self.__LIST_OF_TYPES
    
    #setters
    def set_deck(self, deck):
        self.__deck = deck
         
    #To string
    def __str__(self):
        temp = ""
        counter = 0
        for card in self.get_deck():
            temp += str(card) + "\n"
            counter +=1
        return "DECK: \n" + temp + "\n\tNumber of cards: " + str(counter)
        
        
    
    
        
    
    