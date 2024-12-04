BASIC FLOW:

        Player --|
                 V
Card -> Deck -> Blackjack -> driver

DESC:
    Card:
        Makes objects with attributes of value, type, and suite

    Deck:
        Takes in Card
        Makes a list full of the card objects. This handles filling the deck (list) with 52 cards, with 13 of each suite.
        The code reappropriates the values of 1,11,12, and 13 and reassigning them to their appropriate values within the deck. (King isn't 13, it's valued as 10)
        Method to shuffle the deck randomly
        Method to deal out a card (return a card) and remove it from the current deck (deck.deal())
        
    Player:
        Holds the current cards (current hand) and calcuates the score of it
        Can add cards to current hand through add_cards(usually deck.deal())
        Has another __str__ method to print out the dealer's hand for the beginning of the game
        Keeps track of current wins

    Blackjack:
        Takes in Deck and Player

        This has the main game loop and game logic:

        game() runs the game
        game_start() basically starts the game (duh). It resets everything and adds two cards to the dealer's and player's hand
        is_game_over() checks for conditions for the game to end. Depending on the situation, it will return a different value (or flag) to game_end().
        game_end() takes in the is_game_over()'s flag to determine to keep going or end the game based off the flag.
        
        The player is the current player and dealer is the dealer/machine (again, duh)
        The player gets to either hit or stand.
        At the end of the game, the player sees the current wins between themselves and the dealer. They get to decide to play again after game_end()
    
    driver:
        Takes in Blackjack
        Runs the game
        Have fun :D

    Most classes have DA, __init__(), helpers, getters, setters, __str__() with a few exceptions:
        
        Blackjack doesn't take anything in it's init because it would just break the game. Might as well just set the DA myself.

        Player has a specialized dealer_str() that only prints out what the dealer would show in the beginning in Blackjack


    But otherwise, I think everything else runs smoothly!
    
 


    



       










                

