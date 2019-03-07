# Python program to shuffle a deck of card using the module random and draw 5 cards

# import modules
from pprint import pprint
import random


########################################
##          Deck Functions            ##
########################################

#__________ Create Deck _______________#

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

def create_deck():
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
                [NUMERALS[i],SUITS[j]]
            )

    return deck

#__________ Suffle Deck _______________#

def suffle_deck(deck):
    random.shuffle(deck)


######################################
##        Main game functions       ##
######################################

#__________ Create Players ____________#

def create_players(players_list):
    #check the number of players in the game
    n_players = len(players_list)
    #pre-allocate an array to store players
    players = [{}]*n_players
    #run through array to create a player with its properties
    for i in range(n_players):
        players[i] = {
            'name': players_list[i],
            'cards': [],
            'hand': []
            }
    return players

#_________ Distribute cards ___________#

#distribute cards for each player and then to the table
def distribute_cards(deck,players):
    #--- First, distribute the cards to all players ---#
    #create a counter to keep track of cards being given
    counter = 0
    for i in range(2): #two cards are going to be given for each player
        for player in players: #iterating through each player
            player['cards'].append(deck[counter])
            counter += 1

    #distribute card to the table
    table_cards = [[]]*5
    for i in range(5):
        if i <= 3:
            table_cards[i] = deck[counter]
        else: #burning cards
            table_cards[i] = deck[counter + 1]
        counter += 1

    return table_cards

####################################
##  checking if there is a match  ##
####################################

# #cards that concerns only with numerals
# SINGLE_PAIR = 'AABCD'
# TWO_PAIR = 'AABBC'
# TRIPLE = 'AAABC'
# FULL_HOUSE = 'AAABB'
# FOUR_OF_A_KIND = 'AAAAB'
# #cards that combine numerals and suits
# STRAIGHT = 'SEQUENCE'
# FLUSH = 'SAME_SUITS'
# STRAIGHT_FLUSH = 'SEQUENCE+SAME_SUITS'
# ROYAL_FLUSH = 'SEQUENCE+SAME_SUITS+HIGH_NUMERALS'

def match_combinations(total_player_cards):
    player_suits = {}
    player_numerals = {}
    for i in range(7):
        #matching all possible numerals combinations
        numeral = total_player_cards[i][0]
        if numeral not in player_numerals:
            player_numerals[numeral] = [total_player_cards[i][1]]
        else:
            player_numerals[numeral].append(total_player_cards[i][1])

        #matching all possible suits combinations
        suit = total_player_cards[i][1]
        if suit not in player_suits:
            player_suits[suit] = [total_player_cards[i][0]]
        else:
            player_suits[suit].append(total_player_cards[i][0])

    return player_numerals, player_suits

 #checking for simple combinations and creating sequence
def check_numerals(hand, player_numerals):
    sequence = []
    # player_hand = []
    for key in player_numerals:
        #checking if the values in each numeral is a hand
        numerals = player_numerals[key]
        len_numerals = len(numerals)
        if len_numerals == 2:
            hand.append('one_pair')
        elif len_numerals == 3:
            hand.append('triple')
        elif len_numerals == 4:
            hand.append('four_of_a_kind')
        else:
            pass
        #creating values to store in sequence
        if key == 'Jack':
            val = [11]
        elif key == 'Queen':
            val = [12]
        elif key == 'King':
            val = [13]
        elif key == 'Ace':
            val = [1,14]
        else:
            val = [key]


        #storing sequence values
        sequence.extend(val)

    return hand, sequence

def check_within_hand(hand):
    # checking for combination of combinations
    if (len(hand) > 1) and ('four_of_a_kind' not in hand):
        n_pairs = 0
        n_triples = 0
        for element in hand:
            if element == 'one_pair':
                n_pairs += 1
            elif element == 'triple':
                n_triples += 1
            else:
                pass

            if n_pairs == 2:
                hand = ['two_pairs']
            elif (n_pairs == 1) and (n_triples == 1):
                hand = ['full_house']
    return hand

def check_suits(hand, player_suits):
    #checking for flush:
    if (len(player_suits) == 1) and ('four_of_a_kind' not in hand):
        hand = ['flush']

    return hand

def check_sequence(sequence,hand):
    #sorting sequence
    sequence.sort()
    #we only look for sequence if we have enough cards to do a straight
    if len(sequence) >= 5:
        #instead of iterating through every card, we can optimize by check "blocks" of cards
        possibilities = len(sequence) - 4
        for i in range(possibilities):
            #setting a boolean to make categorize if it is a valid sequence or not
            bool = False
            #if the difference between the numerals of the card don't match, we ignore
            if sequence[i+4]-sequence[i] != 4:
                pass
            else:
                #now that we have a possible sequence, we need to check if the numbers are ordered
                for j in range(4):
                    val = j + i
                    #if the difference between the next number and the current number is 1, they are in order
                    diff = sequence[val+1] - sequence[val]
                    if diff != 1:
                        bool = False
                        #if the difference is not in order, we do not need to continue the loop, so break it
                        break
                    else:
                        bool = True

                #now that we have a valid sequence, we still need to define if it is a straight, straight flush or royal_flush
                if (bool == True):
                    if ('flush' in hand) and (sequence[i] == 10):
                        hand = ['royal_flush']
                    elif ('flush' in hand) and ('four_of_a_kind' not in hand):
                        hand = ['straight flush']
                    elif ('four_of_a_kind' not in hand):
                        hand = ['straight']
                    else:
                        pass
                    break

    return hand

def check_combinations(player_numerals, player_suits):
    hand = []
    hand, sequence = check_numerals(hand,player_numerals)
    hand = check_within_hand(hand)
    hand = check_suits(hand, player_suits)
    if len(hand) < 1:
        hand = ['high_card']

    return hand

def check_player_hand(player):
    #create a list that combines the cards in the cards of the player and the cards on table
    total_player_cards = player['cards'] + table_cards
    player_numerals, player_suits = match_combinations(total_player_cards)
    hand = check_combinations(player_numerals,player_suits)
    player['hand'] = hand

def print_game(players, table_cards):
    #Print it in a beautiful way:

    print('Cards on the table are: ')
    for card in table_cards:
        print(' '*5 + str(card[0]) + ' of ' + str(card[1]))

    print(' ')
    print('These are the players: ')
    for player in players:
        print('- - - - - - - - - - - -')
        print(' '*2 + 'Player: ' + player['name'])
        print(' '*5 + 'Player cards are: ')
        for card in player['cards']:
            print(' '*10 + str(card[0]) + ' of ' + str(card[1]))
        print(' '*5 + 'Player hand is: ')
        hand = player['hand'][0]
        if hand.find("_") != -1:
            hand = hand.split("_")
            hand[0] = hand[0][0].upper() + hand[0][1:]
            hand[1] = hand[1][0].upper() + hand[1][1:]
            hand = hand[0] + ' ' + hand[1]
        print(' '*10 + hand)



if __name__ == '__main__':

    #set a list of players with their names
    players_list = ['1', '2', '3', '4', '5']
    #create a deck!
    deck = create_deck()
    #suffle the cards on the deck
    suffle_deck(deck)
    #create players
    players = create_players(players_list)
    #distribute the cards to all players and to the table
    table_cards = distribute_cards(deck,players)

    #now check the hand of every player
    for player in players:
        check_player_hand(player)

    #print the game in a nice format
    print_game(players,table_cards)
