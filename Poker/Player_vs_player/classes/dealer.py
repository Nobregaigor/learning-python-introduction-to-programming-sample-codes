class Dealer():
    def __init__(self):
        self.name = 'Bob, the Dealer!'

    def distribute_cards(self,deck,players,table):
        #--- Suffle Deck ---#
        deck.suffle()

        #--- Distribute the cards to all players ---#
        #create a counter to keep track of cards being given
        counter = 0
        for i in range(2): #two cards are going to be given for each player
            for key in players: #iterating through each player
                player = players[key]
                card = deck.cards[counter]
                card.status = 'on_hand'
                player.cards.append(card)
                counter += 1

        #--- Distribute the cards to table ---#
        for i in range(5):
            if i <= 3:
                card = deck.cards[counter]
                card.status = 'folded'
                table.cards[i] = card
            else: #burning cards
                card = deck.cards[counter]
                card.status = 'folded'
                table.cards[i] = card
            counter += 1

    def unfold_card(self,card):
        card.status = 'unfolded'

    def unfold_cards(self,table,round):
        if round == 0:
            for i in range(3):
                table.cards[i].status = 'unfolded'
        elif round == 1:
            table.cards[3].status = 'unfolded'
        elif round == 2:
            table.cards[4].status = 'unfolded'
        else:
            raise ValueError('Wrong round provided to the dealer. Please, check it again')
