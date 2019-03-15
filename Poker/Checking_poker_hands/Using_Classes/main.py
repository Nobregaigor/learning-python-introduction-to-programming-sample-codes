from classes.deck import Deck
from classes.cards import Card
from classes.player import Player
from classes.dealer import Dealer
from classes.table import Table
from classes.game import Game


if __name__ == '__main__':
    game = Game()
    game.build(5)
    game.dealer.distribute_cards(game.deck,game.players,game.table)
    game.players['bot0'].check_hand(game.table)
