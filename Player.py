class Player:
    
    #DA
    __hand = []
    __score = 0
    __wins = 0

    
    #Init
    def __init__(self, hand, score, wins):
        self.set_hand(hand)
        self.set_score(score)
        self.set_wins(wins)

        
    
    #Helpers
    
    #Add card to the current hand
    def add_cards(self, card):
        self.get_hand().append(card)
        
    #Calcualte score based on current hand
    def calculate_score(self):
        temp = 0
        
        for card in self.get_hand():
            
            #Check for aces
            #If an ace, set to 11
            if (isinstance(card.get_value(),list ) == True):
                temp += card.get_value()[1]
                
            #Otherwise, set the value
            else:
                temp+=card.get_value()
            
        #If there's an ace in the hand and the current score is above 21
        #Subtract 10 from score
        #(Ace becomes a 1)
        for i in range(len(self.get_hand())):
            if (temp > 21 and isinstance(self.get_hand()[i].get_value(), list) == True):
                temp -= 10
    
        #Set the score
        self.set_score(temp)
        
        
    #To string for dealer (Used only at beginning of game)
    def dealer_str(self):
        temp = self.get_hand()[0]

        return str(temp)+ "\n\nScore: " + str(self.get_hand()[0].get_value()) + " + ?" + "\n"
    
        
    #Getters
    def get_hand(self):
        return self.__hand

    def get_score(self):
        return self.__score
    
    def get_wins(self):
        return self.__wins
    
    
    
    #Setters    
    def set_hand(self, hand):
        self.__hand = hand
    
    def set_score(self, score):
        self.__score = score
        
    def set_wins(self, w):
        self.__wins = w
    
    #To string
    def __str__(self):
        temp = ""
        for card in self.get_hand():
            temp += str(card) + "\n"
            
        return temp + "\nScore: " + str(self.get_score()) + "\n"
    

    
  
        
    
                
    
        
            
    
        
        
        
        
    
    