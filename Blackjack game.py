#Blackjac game
import random

#Define common attributes of cards
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10,
           'King':10, 'Ace':11}
playing = True

#Card class to create each card
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.suit +' of '+ self.rank

#Test of above block
'''testcard = Card('Hearts','Two')
print(testcard)'''

#Deck class for 13 pair of cards of each suits
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_card = ''
        for card in self.deck:
            deck_card +='\n '+card.__str__()
        return 'Cards in deck: '+deck_card
    
    def card_shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        single_card = self.deck.pop()
        return single_card

'''#test of above block    
testdeck = Deck()
testdeck.card_shuffle()
#print(len(testdeck.all_cards))
card1 = testdeck.deal_one()
print(card1)'''


#Hand class for playing card of player and dealer
class hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    #add card and check if it is aces
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    #if ace card added and value > 21 : ace value = 1
    def check_ace(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
'''
test_player = hand()
test_player.add_card(testdeck.deal_one())
test_player.add_card(testdeck.deal_one())
print(test_player.value)
for card in test_player.card:
    print(card)'''


#class chips for 
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

#take bet and check bet amt
def take_bet(chips):
    print('\nYour total chips are ',chips.total)
    while True:
        try:
            chips.bet = int(input('Please provide your bet amount: '))
        except ValueError:
            print('Bet value must be integer.')
        else:
            if chips.bet > chips.total:
                print('You are out of total amount in Acc.',chips.total)
            else:
                break

#hit card
def hit(deck,hand):
    hand.add_card(deck.deal_one())
    hand.check_ace()

#hit or stand
def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input('\nWould ou like to Hit or Stand. Enter h or s: ')
        if x[0].lower() == 'h':
            print('\nPlayer hits.')
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('\nplayer stands. Dealer is playing.')
            playing = False
        else:
            print('Incorrect input.')
            continue
        break

def show_some(player, dealer):
    print('\nDealer cards: ')
    print('<1st card is hidden>')
    print('',dealer.cards[1])
    print('\nPlayer cards: ',*player.cards, sep='\n')

def show_all(player, dealer):
    print('\nDealer hand: ',*dealer.cards, sep='\n')
    print('Dealer value: ',dealer.value)
    print('\nPlayer hand: ',*player.cards, sep='\n')
    print('Player value: ',player.value)

def player_bust(player,dealer,chips):
    print('\nPlayer busts.')
    chips.lose_bet()

def player_win(player,dealer,chips):
    print('\nPlayer wins.')
    chips.win_bet()

def dealer_bust(player,dealer,chips):
    print('\nDealer busts. Player wins!!!')
    chips.win_bet()

def dealer_win(player,dealer,chips):
    print('\nDealer wins. Player lose!!!')
    chips.lose_bet()

def tie(player,dealer,chips):
    print('\nPlayer and dealer tie.')

while True:
    #input statement
    print('!!! Welcome to Blackjack Game !!!')

    #deck creation
    deck = Deck()
    deck.card_shuffle()

    #hand creation for player & dealer.Also adding cards
    player_hand = hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())

    dealer_hand = hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

    #Set chips for player
    player_chips = Chips()

    #take bet from player
    take_bet(player_chips)

    #show cards but 1 dealer card hidden
    show_some(player_hand,dealer_hand)

    #while playing loop
    while playing:

        #Ask player for hit or stand
        hit_or_stand(deck,player_hand)

        #show cards but 1 dealer card hidden
        show_some(player_hand,dealer_hand)

        #player cards > 21: bust player and break loop
        if player_hand.value>21:
            player_bust(player_hand,dealer_hand,player_chips)
            break
    
    #if player < 21 then play dealers hand until dealer >= 17 
    if player_hand.value <= 21:
    
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        #show all cards
        show_all(player_hand,dealer_hand)

        #dealer value > 21 then all scenerio
        if dealer_hand.value > 21:
            dealer_bust(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_win(player_hand,dealer_hand,player_chips)
        
        else:
            tie(player_hand,dealer_hand,player_chips)
    
    print('\nPlayer total chips: ',player_chips.total)
    #input to continue playing
    new_game = input('\nDo you want to play again. Enter y and n: ')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('-------------')
        print('Thnaks for playing.')
        break