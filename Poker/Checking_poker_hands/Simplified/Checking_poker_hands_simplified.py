# Python program to shuffle a deck of card using the module random and draw 5 cards

# import modules
from pprint import pprint
import random


##############################
##      Creating Deck       ##
##############################

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

#Take a look at the entire deck!
print("This is the entire deck:\n")
pprint(deck)
print(" ")
print("="*40 + '\n')

##############################
##       Suffle Deck        ##
##############################

# shuffle the deck
random.shuffle(deck)
print("This is the deck suffled:\n")
pprint(deck)
print(" ")
print("="*40 + '\n')


##############################
##    Distribute cards      ##
##############################

#set number of players, remember that the max number of players is 22, and in a cassino is usually max of 12
n_players = 5

#create players
player1 = {'name': '1', 'cards': [], 'hand': []}
player2 = {'name': '2', 'cards': [], 'hand': []}
player3 = {'name': '3', 'cards': [], 'hand': []}
player4 = {'name': '4', 'cards': [], 'hand': []}
player5 = {'name': '5', 'cards': [], 'hand': []}

#create an array of players
players = [player1, player2, player3, player4, player5]

#distribute cards for each player
#create a counter to keep track of cards being given
counter = 0
for i in range(2): #two cards are going to be given for each player
    for player in players: #iterating through each player
        player['cards'].append(deck[counter])
        counter += 1

print("These are all the players:\n")
pprint(players)
print(" ")
print("="*40 + '\n')

print("These are your cards (player 1):\n")
pprint(player1['cards'])
print(" ")
print("="*40 + '\n')

#distribute card to the table
table_cards = []
for i in range(5):
    if i <= 3:
        table_cards.append(
            deck[i + n_players*2]
            )
    else:
        table_cards.append(
            deck[i + n_players*2 + 1] #burning cards
            )

print("These are the cards on table:\n")
pprint(table_cards)
print(" ")
print("="*40 + '\n')


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

for player in players:
    player_suits = {}
    player_numerals = {}
    hand = []
    sequence = []

    #create a list that combines the cards in the cards of the player and the cards on table
    total_player_cards = player['cards'] + table_cards

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


    # print('player numerals')
    # print(player_numerals)
    # print('player suits')
    # print(player_suits)

    #checking for simple combinations and creating sequence
    for key in player_numerals:
        numerals = player_numerals[key]
        if len(numerals) == 2:
            hand.append('one_pair')
        elif len(numerals) == 3:
            hand.append('triple')
        if len(numerals) == 4:
            hand.append('four_of_a_kind')

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

        sequence.extend(val)


    #checking for combination of combinations
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

    #checking for flush:
    if (len(player_suits) == 1) and ('four_of_a_kind' not in hand):
        hand = ['flush']

    #checking for sequence
    #sorting sequence
    sequence.sort()
    # print('sequence')
    # print(sequence)

    if len(sequence) >= 5:
        possibilities = len(sequence) - 4
        # print('possibilities = '+ str(possibilities))
        for i in range(possibilities):
            bool = False
            # print('sequence i = ' + str(i))
            if sequence[i+4]-sequence[i] != 4:
                pass
            else:
                for j in range(4):
                    val = j + i
                    # print('j: ' + str(j))
                    diff = sequence[val+1] - sequence[val]
                    # print('sj+1: ' + str(sequence[val+1]))
                    # print('sj: ' + str(sequence[val]))
                    # print('diff: ' + str(diff))
                    if diff != 1:
                        bool = False
                        break
                    else:
                        bool = True

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

    if len(hand) < 1:
        hand = ['high_card']

    player['hand'] = hand[0]


print("These are the players and their hands:\n")
pprint(players)
print(" ")
print("="*40 + '\n')
print("="*40 + '\n')
print("="*40 + '\n')

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
    hand = player['hand']
    if hand.find("_") != -1:
        hand = hand.split("_")
        hand[0] = hand[0][0].upper() + hand[0][1:]
        hand[1] = hand[1][0].upper() + hand[1][1:]
        hand = hand[0] + ' ' + hand[1]

    print(' '*10 + hand)
