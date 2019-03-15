from pprint import pprint
class Card():
    def __init__(self,numeral,suit,value):
        self.numeral = numeral
        self.suit = suit
        self.value = value
        self.status = None

    def print(self):
        print('Card: ' + str(self.numeral) + ' of ' + self.suit + '; value = ' + str(self.value) + ' , status = ' + self.status)
