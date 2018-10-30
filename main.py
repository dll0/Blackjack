import random

class Deck(object):
    def __init__(self):
        self.deck_of_cards = list()
        letter = {0: 'A', 10: 'J', 11: 'Q', 12: 'K'}
        suit =  {0: '.H', 1: '.D', 2: '.C', 3: '.S'}

        for i in range(0, 4):
            for j in range(0,13):
                if not j in (0, 10, 11, 12):
                    self.deck_of_cards.append(str(j+1)+suit.get(i))
                else:
                    self.deck_of_cards.append(letter.get(j)+suit.get(i))


    def print_deck(self):
        print(self.deck_of_cards)


    def get_card(self, quantity):
        self.quantity = quantity
        cards = list()
        for i in range(0, self.quantity):
            var = self.deck_of_cards.pop(-1)
            cards.append(var)
            #self.deck_of_cards.insert(0, var) --READICIONAR CARTAS AO BARALHO QUANDO EMBARALHAR
        return cards


    def card_shuffle(self):
        self.deck_of_cards = random.sample(self.deck_of_cards, len(self.deck_of_cards))

    
    def draw_card(self, card):
        self.card = card
        for items in self.card:
            suit = items[2]
            card = items[0]

        print('-' * 20)
        for i in range(0, 12):
            print('|', end='')
            print(suit.center(' ', 20), end='')
            print(card, end='')
            print('|', end='')
        print('-' * 20)
            
            
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
    print('.' * 150)

print(' Blackjack(21) '.center(150, '+'))

for i in range(0,2):
    print('.' * 150)

dck = Deck()
dck.card_shuffle()
card = dck.get_card(1)
print(card)
dck.print_deck()
dck.draw_card(card)
