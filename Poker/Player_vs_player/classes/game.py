from deck import Deck
from cards import Card
from player import Player
from dealer import Dealer
from table import Table

from pprint import pprint

class Game():
    def __init__(self):
        self.players = {}
        self.deck = Deck()
        self.dealer = Dealer()
        self.table = Table()
        self.big_blind = 1
        self.small_blind = 0
        self.active_players = []

    def load_players(self,n_players, list=[]):
        n_list = len(list)
        for i in range(n_players):
            if i < n_list:
                name = list[i]
                self.players[name] = Player(name, 'human')
            else:
                name = 'bot' + str(i)
                self.players[name] = Player(name, 'bot')

            self.dealer.pay_player(self.players[name],500)

    def build(self,n_players,players=[]):
        self.deck.build()
        self.load_players(n_players,players)

    def start_turn(self):
        self.dealer.distribute_cards(self.deck,self.players,self.table)

    def update_active_players(self,player):
        if player.status != 'folded':
            self.active_players.append(player.name)

    def player_bets(self):
        self.active_players = []
        for key in self.players:
            player = self.players[key]
            if player.status != 'folded':
                print(" ")
                print("Player: " + player.name)
                print('- These are your cards: ')
                for card in player.cards:
                    card.pretty_print()
                player.check_hand(self.table)
                print("- This is your hand: " + str(player.hand[0]))
                print("- This is your money: " + str(player.money))
                print("- This is the current bet: " + str(self.table.current_bet) + '\n')
                res = input(player.name + ', this is your turn! Make a wise choice. {bet, increase, cover, pass, fold} \n')
                vals = res.split(' ')
                if len(vals) > 1:
                    move = player.play_turn(self.table, vals[0],int(vals[1]))
                else:
                    move = player.play_turn(self.table, vals[0])
            self.update_active_players(player)

    def check_active_players(self):
        if len(self.active_players) != 1:
            return True

    def display_unfolded_cards(self,table):
        for card in table.cards:
            if card.status == 'unfolded':
                card.pretty_print()

    def play_turn(self):
        print("====== Starting turn ======")
        self.start_turn()
        print("Initial bet: ")
        self.player_bets()
        if self.check_active_players() == True:
            print("\n"*15)
            for i in range(3):
                if self.check_active_players() == True:
                    print('\n----------------')
                    print("Unfolding cards [" + str(i) + "]")
                    print("----------------\n")
                    self.dealer.unfold_cards(game.table,i)
                    print("These are the cards on the table: ")
                    self.display_unfolded_cards(game.table)
                    print("Current bet amount: " + str(game.table.current_bet))
                    self.player_bets()
                    print("\n"*15)
                else:
                    print('\n\nPlayer ' + self.active_players[0] + ' won this round')
        else:
            print('\n\nPlayer ' + self.active_players[0] + ' won this round')





if __name__ == '__main__':
    game = Game()
    game.build(2,['igor','bob'])
    game.play_turn()

    # game.dealer.distribute_cards(game.deck,game.players,game.table)
    # game.players['igor'].check_hand(game.table)
    # game.dealer.unfold_cards(game.table,0)
    # game.players['igor'].check_hand(game.table)
    # print(game.players['igor'].hand)
    # game.dealer.unfold_cards(game.table,1)
    # game.players['igor'].check_hand(game.table)
    # print(game.players['igor'].hand)
    # game.players['igor'].money = 1000
    # game.table.current_bet = 50
    # print(game.players['igor'].bet_amount)
    # game.players['igor'].play_turn(game.table, 'bet',80)
    # print(game.players['igor'].bet_amount)
