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


    def load_players(self,n_players, list=[]):
        n_list = len(list)
        for i in range(n_players):
            if i < n_list:
                name = list[i]
                self.players[name] = Player(name, 'human')
            else:
                name = 'bot' + str(i)
                self.players[name] = Player(name, 'bot')

    def build(self,n_players,players=[]):
        self.deck.build()
        self.load_players(n_players,players)


if __name__ == '__main__':
    game = Game()
    game.build(5,['igor'])
    game.dealer.distribute_cards(game.deck,game.players,game.table)
    game.players['igor'].check_hand(game.table)
