import random

class Deck(object):
    def __init__(self):
        self.deck_of_cards = []
        self.base = []
        for i in range(0,13):
            troca = {0: 'A', 10: 'J', 11: 'Q', 12: 'K'}
            if not i in (0, 10, 11, 12):
                self.base.append(i+1)
            else:
                self.base.append(troca.get(i))
            
        for i in range(0, 4):
            self.deck_of_cards.append(self.base.copy())


    def print_deck(self):
        for i in range(0, len(self.deck_of_cards)):
            suit = self.deck_of_cards[i]
            switch = {0: 'Espadas: ', 1: 'Paus: ', 2: 'Copas: ', 3: 'Ouros: '}
            string = switch.get(i)
            print(string, suit)


    def random_card(self, quantity):
        self.quantity = quantity
        for i in range(0, self.quantity):
            size_suit = len(self.deck_of_cards) > 0
            if size_suit:
                d = 1
            else:
                exit('Baralho simplesmente acabou, como tu fez isso em um blackjack cidadão???') #Isso nunca vai acontecer, mas tamo aí
            suit = random.randint(0, len(self.deck_of_cards) - d)

            size_card = len(self.deck_of_cards[suit]) > 0
            if size_card:
                d = 1
            else:
                d = 0
                self.deck_of_cards[suit] = []
                print(self.deck_of_cards)
            card = random.randint(0, len(self.deck_of_cards[suit]) - d)

            self.deck_of_cards[suit].pop(card)
            
            

class Player(object):
    def __init__(self, name, age, cash):
        self.name = name
        self.age = age
        self.cash = cash

    def print_player(self):
        print('Olá {}, você depositou R${:.2f}!'.format(self.name, self.cash))


class Hand(object):
    def __init__(self, cards):
        self.hand = list()
        self.cards = cards
        for items in self.cards:
            self.hand.append(items)

    def hand_value(self):
        return sum(self.hand)


for i in range(0,2):
    print('=' * 150)

print(' Bem-vindo ao BlackJack(21) em Python '.center(150, '='))

for i in range(0,2):
    print('=' * 150)

dck = Deck()

for i in range(0, 90):
    dck.random_card(1)
    print('')
    dck.print_deck()

