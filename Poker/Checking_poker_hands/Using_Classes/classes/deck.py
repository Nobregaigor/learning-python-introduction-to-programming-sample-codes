from cards import Card
import random

class Deck():

    def __init__(self):
        self.cards = []


    def build(self):
        #set number of cards
        n_cards = 52
        #Number of suits in a deck
        n_Suits = 4
        #Number of cards for each suit
        n_Cards_for_Suits = 13
        #create a list of suits
        SUITS = ['Spade','Heart','Diamond','Club']
        #create a list of court
        COURT = ['Jack','Queen','King']
        #create a list of numerals
        NUMERALS = list(range(2, n_Cards_for_Suits - 3)) #We are subtracting 3 because we are adding the court to the numerals
        NUMERALS.insert(0,'Ace')
        NUMERALS.extend(COURT)

        #create deck
        deck = []
        for i in range(n_Cards_for_Suits - 1): #Subtracting one because counter starts at 0
            for j in range(n_Suits):
                deck.append(
                    Card(NUMERALS[i],SUITS[j],i+1)
                )

        self.cards = deck

    def suffle(self):
        random.shuffle(self.cards)


# if __name__ == '__main__':
#     deck = Deck()
#     deck.build()
#     deck.suffle()
#     # for i in range(len(deck.cards)):
#     #     deck.cards[i].print()
