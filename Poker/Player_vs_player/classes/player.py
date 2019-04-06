from pprint import pprint
class Player():
    def __init__(self, name,type):
        self.name = name
        self.type = type
        self.cards = []
        self.hand = []
        self.money = []
        self.bet_amount = 0
        self.action = None
        self.status = None


    ############################################

    def match_combinations(total_player_cards):
        player_suits = {}
        player_numerals = {}
        n = len(total_player_cards)
        for i in range(n):
            #matching all possible numerals combinations
            numeral = total_player_cards[i].numeral
            if numeral not in player_numerals:
                player_numerals[numeral] = [total_player_cards[i].numeral]
            else:
                player_numerals[numeral].append(total_player_cards[i].numeral)

            #matching all possible suits combinations
            suit = total_player_cards[i].suit
            if suit not in player_suits:
                player_suits[suit] = [total_player_cards[i].suit]
            else:
                player_suits[suit].append(total_player_cards[i].suit)

        return player_numerals, player_suits

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
            if (len(player_suits.values()) == 4):
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
        hand, sequence = Player.check_numerals(hand,player_numerals)
        hand = Player.check_within_hand(hand)
        hand = Player.check_suits(hand, player_suits)
        if len(hand) < 1:
            hand = ['high_card']

        return hand

    def check_hand(self,table):
        #create a list that combines the cards in the cards of the player and the cards on table
        unfolded_cards = []
        for card in table.cards:
            if card.status == 'unfolded':
                unfolded_cards.append(card)

        total_player_cards = self.cards + unfolded_cards

        player_numerals, player_suits = Player.match_combinations(total_player_cards)
        self.hand = Player.check_combinations(player_numerals,player_suits)

    def check_money(self,value):
        if (self.money > value):
            return True
        else:
            return False

    def bet(self,table,value):
        if self.check_money(value) == True:
            self.action = 'betting'
            self.bet_amount = value
            self.money -= value
            table.current_bet = value
            table.money += value
            return value
        else:
            print("Sorry "+ self.name + ", you don't have enough money to bet this amount")
            return -1

    def increase_bet(self,table,value):
        if self.check_money(value) == True:
            self.action = 'increasing_bet'
            new_bet = table.current_bet + value
            self.money -= new_bet
            self.bet_amount = new_bet
            table.current_bet = new_bet
            table.money += new_bet
            return new_bet
        else:
            print("Sorry "+ self.name + ", you don't have enough money to bet this amount")
            return -1

    def cover_bet(self,table):
        if self.check_money(table.current_bet) == True:
            self.action = 'covering_bet'
            value = table.current_bet - self.bet_amount
            #update bet amount
            self.bet_amount = table.current_bet
            self.money -= value
            table.money += value
            return value
        else:
            print("Sorry "+ self.name + ", you don't have enough money to bet this amount")
            return -1

    def play_turn(self,table,move,value=0):
        if move == 'bet':
            self.status = 'participating'
            return self.bet(table,value)
        elif move == 'increase':
            self.status = 'participating'
            return self.increase_bet(table,value)
        elif move == 'cover':
            self.status = 'participating'
            return self.cover_bet(table)
        elif move == 'pass':
            self.status = 'participating'
            self.action = 'passing'
            return 'pass'
        elif move == 'fold':
            self.status = 'folded'
            self.action = 'folding'
            return 'fold'
        else:
            print("Sorry "+ self.name + ", this was an invalid move")
            return -1
