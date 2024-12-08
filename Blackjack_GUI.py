from Deck import Deck
from Player import Player
from tkinter import *
from functools import partial
import pygame

class Blackjack_GUI:
    
    #init
    #There's not really a reason to bring in variables to set in the init since it would kind of just break the game
    #Soooo everything is automatically set :)
    def __init__(self):
        self.set_can_reset(False)
        self.set_standing(False)
        self.init_music()
        self.game_init()

#--------------------------------------GAME-------------------------------------------------------------------------------------------------------------------------
    #Helpers
    def game_init(self):
        
        #Declare variables and make objects for game
        deck = Deck([])
        player = Player([], 0, 0)
        dealer = Player([] ,0, 0)
        
        #MAKE THE WINDOW!!!
        top = Tk()
        top.title("Braxton's Black Jack :)")
        top.geometry("1200x750")
        
        current_hand_label = Label(top, text="~~~~~~~~~~~CURRENT HAND~~~~~~~~~~~")
        dealer_hand_label = Label(top, text=" ~~~~~~~~~~~DEALER'S HAND~~~~~~~~~~")
        player_choices_label =Label(top,text="~~~~~~~~~~PLAYER OPTIONS~~~~~~~~~~")
        game_label = Label(top, text="~~~~~~~~~~~~~~~~~~~~~GAME WINDOW~~~~~~~~~~~~~~~~~~~~~")
        
        
        player_box = Text(top, height = 30, width = 30)
        dealer_box = Text(top, height = 30, width = 30)
        desc_box = Text(top, height = 30, width = 80)
        
        btn1 = Button(top, text="HIT", command=partial(self.hit, top, player, dealer, deck))
        btn2 = Button(top, text="STAND", command = partial(self.stand, top, player, dealer, deck))
        btn3 = Button(top, text="HELP!!", command = partial(self.help, top))
        btn4 = Button(top, text="RESET", command = partial(self.reset, top, dealer, player, deck))
        
        
        current_hand_label.grid(column=0, row=0, padx=5, pady=5)
        dealer_hand_label.grid(column = 1, row = 0, padx=5,pady=5)
        player_choices_label.grid(column=0, row=4, padx=5, pady=5)
        game_label.grid(column=2,row=0,padx=5,pady=5)
        
        player_box.grid(column = 0, row = 1)
        desc_box.grid(column = 2, row = 1)
        dealer_box.grid(column = 1, row = 1)
        
        btn1.grid(column=0, row=5, padx=10,pady=10)
        btn2.grid(column=0,row=6, padx=10,pady=10)
        btn3.grid(column=0,row=7, padx=10,pady=10)
        btn4.grid(column=0, row=8, padx=15, pady=15)
        
        #Start game
        self.game(top,dealer,player,deck)
        
        #Start window
        top.mainloop()
          
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
#----------------------MAIN GAME LOOP-----------------------------------------------------------------------------------------------------------------------------
    def game(self, top, dealer, player, deck): 
        #Start game and check for immediate win
        self.game_start(dealer, player, deck)
        self.game_end(self.is_game_over(dealer, player),top, dealer, player, deck)
        
        #Set top's children to be object that can be modifed
        #I don't need to do this, but it just makes it a little clearer on what I'm doing
        player_box = top.children['!text']
        dealer_box = top.children['!text2']
        
        dealer_box.insert('1.0',dealer.dealer_str())
        player_box.insert('1.0',player)
        

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
                  
    #The dealer tries to beat player's current score
    def dealer_turn(self,top,dealer, player, deck):
        
        #While the machine's score is less than  player's score and the machine isn't at 21
        while (dealer.get_score() < player.get_score() and dealer.get_score() < 21):
            
            #Add another card to the dealer's hand and calculate score
            dealer.add_cards(deck.deal())
            dealer.calculate_score()
        
        #Print the dealer's current hand
        top.children['!text2'].delete("1.0", END)
        top.children['!text2'].insert("1.0", dealer)
        
        #Return whether the game ended
        return (self.is_game_over(dealer, player))
    
#---------------------GAME LOGIC----------------------------------------------------------------------------------------------------------
                
    def game_start(self, dealer, player, deck):
        #Basically, reset everything
        dealer.set_hand([])
        player.set_hand([])
        
        deck.set_deck(deck.build_deck([]))
        deck.shuffle()
        
        #Set standing to false
        self.set_standing(False)
        
        #Deal two cards to both the player and machine and also calculate the scores
        dealer.add_cards(deck.deal())
        dealer.add_cards(deck.deal())
        
        dealer.calculate_score()
        
        player.add_cards(deck.deal())
        player.add_cards(deck.deal())
        
        player.calculate_score()
    
    def init_music(self):
        #Add music
        theme = 'audio/rock_this_town.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(theme)
        pygame.mixer.music.play()



    #Determine if the game is over and return a value that describes what happened
    def is_game_over(self, dealer, player):
        
        #Tells what happened to end the game if the game does end
        what_happened = 0
        
        #If the machine gets 21
        if (dealer.get_score() == 21):
            dealer.set_wins(dealer.get_wins() + 1)
            what_happened = 1
            
        #If the machine busts out
        elif (dealer.get_score() > 21):
            player.set_wins(player.get_wins() + 1)
            what_happened = 2
            
        #If the player busts
        elif (player.get_score() > 21):
            dealer.set_wins(dealer.get_wins() + 1)
            what_happened = 3
            
        #If the player gets 21  
        elif (player.get_score() == 21):
            player.set_wins(player.get_wins() + 1)
            what_happened = 4

        #If the machine got more points than the player while the player is standing
        elif (dealer.get_score() > player.get_score() and self.get_standing()):
            dealer.set_wins(dealer.get_wins() + 1)
            what_happened = 5
        
        #If draw
        elif (dealer.get_score() == player.get_score() and self.get_standing()):
            what_happened = 6
            
        return what_happened
          

    def game_end(self, what_happened, top, dealer, player, deck):
        
        #If the game did actually end
        if (what_happened != 0):
            
            #Concatenate string
            temp = ""

            #Print ending hands
            temp +="    DEALERS-HAND    \n"
            temp += str(dealer)
            temp += "\n"
            
            
            temp += "\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
            temp += "\t[               G A M E  O V E R ! ! !              ]\n"
            temp += "\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        
            #Determine what happened
            if (what_happened == 1):
                temp += "\n\t\t| Dealer got 21! |\n"
            elif (what_happened == 2):
                temp += "\n\t\t| Dealer busts! |\n"
            elif (what_happened == 3):
                temp += "\n\t\t| Player busts!  |\n"
            elif (what_happened == 4):
                temp += "\n\t\t| Player got 21!  |\n"
            elif (what_happened == 5):
                temp+= "\n\t\t| Dealer scored higher than player! |\n"
            elif (what_happened== 6):
                temp+= "\n\t\t| Dealer's score matched player's score! |"
                
            #Troubleshooting
            else:
                temp +="\n\t\t| Game ended... somehow?? Good job Braxton!!! |"
                
                
            #Calculate how many wins the player and machine have        
            temp += "\n\t\t\tDealer: " + str(dealer.get_wins()) + "\n\t\t\tPlayer: " + str(player.get_wins())
        
            #Print game over string
            top.children['!text3'].delete('1.0',END)
            top.children['!text3'].insert('1.0', temp)
            self.set_can_reset(True)
            
            
#---------------MAIN BUTTONS----------------------------------------------------------------
    def hit(self, top, player, dealer, deck):
        
        if self.get_can_reset() != True:
            player.add_cards(deck.deal())
            player.calculate_score()
            
            top.children['!text'].delete('1.0', END)
            top.children['!text'].insert('1.0',player)
            self.game_end(self.is_game_over(dealer,player),top, dealer, player, deck)
            
        else:
            top.children['!text3'].delete('1.0',END)
            top.children['!text3'].insert('1.0', "One must imagine... resetting...")
        
    
    def stand(self, top, player, dealer, deck):
        
        if self.get_can_reset() != True:  
            self.set_standing(True)
            self.game_end(self.dealer_turn(top, dealer, player, deck), top, dealer, player, deck)
        else:
            top.children['!text3'].delete('1.0',END)
            top.children['!text3'].insert("1.0", "Don't break my game!, reset!!!")
        
        
    def help(self, top):
        temp = ""
        temp += "\nGAME INFO-----------------------------------------------------------------------------------------------------------\n\n"
        temp += "Rules:\n"
        temp += "   The goal of blackjack is to beat the dealer's score while keeping your own score below 22.\n"
        temp += "   The maximum score a player can get is 21. Going past 21 means that you bust (lose).\n"
        temp += "   Score is calculated by the value of the card (number cards = number, Face cards = 10, and Aces can be 1 or 11).\n\n"
        temp += "   At the beginning, you and the dealer are both dealt 2 cards. It is possible to achieve 21 from 2 cards, which is an automatic win!\n"
        temp += "   If neither you or the dealer have an automatic 21, the game continues.\n\n"
        temp += "   You are given the options of hitting or standing\n\n"
        temp += "Hitting:\n"
        temp += "   Hitting means to draw another card and add it to your hand. This will increase your score (remember not to go over 21!).\n"
        temp += "   The dealer will hit at the end of your turn after you decide to stand.\n\n"
        temp += "Standing:\n"
        temp += "   Standing means that you are locking in your current score to try and beat the dealer's unknown/undecided score.\n"
        temp += "   Before standing, you're only able to see ONE of the dealers cards.\n"
        temp += "   After standing, the dealer will reveal his cards and draw cards to try to either match your score or beat your score.\n"
        temp += "   If the dealer's score is greater than yours after standing, you lose. If the dealer's score goes over 21, you win. Else, it's a draw.\n\n"
        temp +="Aces:\n"
        temp +="    As said earlier, Aces can either count as 1 or 11 (You'll see it as [1,11]).\n"
        temp +="    If you have an Ace in your hand and you go over 21 while hitting, the Ace now counts as a 1. Else, it counts as 11.\n\n"
        temp +="\nEND OF GAME INFO----------------------------------------------------------------------------------------------------\n\n"
        
        desc_box = top.children['!text3']
        desc_box.delete("1.0", END)
        desc_box.insert("1.0", temp)
        
    def reset(self, top, dealer, player, deck):
        
        if self.get_can_reset():
            top.children['!text'].delete("1.0", END)
            top.children['!text2'].delete("1.0",END)
            top.children['!text3'].delete("1.0", END)
            self.set_can_reset(False)
            self.game(top, dealer, player, deck)
            
        else:
            top.children['!text3'].delete("1.0", END)
            top.children['!text3'].insert("1.0", "No resetting for you!!!")
        
#--------------------------------------------------------------------------------------------------------------------- 

    #Getters
    def get_can_reset(self):
        return self.__reset

    def get_standing(self):
        return self.__standing
    
    #Setters
    def set_can_reset(self, reset):
        self.__reset = reset
     
    def set_standing(self, standing):
        self.__standing = standing

    def __str__(self):
        return "Black Jack Game Settings:\n\tStanding: " + str(self.get_standing()) + "\n\tCan reset?: " + str(self.get_can_reset())
        
        
        

    

        
                
        
