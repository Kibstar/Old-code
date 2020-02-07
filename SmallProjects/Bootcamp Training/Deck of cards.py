from random import shuffle



class Card:
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
        if rank == 'Ace':
            self.value = 11
        elif rank in ['King', 'Queen', 'Jack']:
            self.value = 10
        else:
            self.value = int(rank)

    @staticmethod
    def deckShuffle():
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        deck = []
        ranks = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit, rank))
        shuffle(deck)
        return deck


class Player:
    startingMoney = 5000

    def __init__(self, name):
        self.name = name
        self.money = Player.startingMoney
        self.handValue = 0

    def winLose(self,amount):
        self.money += amount


def bust(cardList):
    cardTotal = 0
    aceCount = 0

    for i in cardList:
        if i.rank == 'Ace':
            cardTotal += i.value
            aceCount += 1
        else:
            cardTotal += i.value
    while aceCount > 0:
        if cardTotal > 21:
            cardTotal -= 10
            aceCount -= 1
        else:
            break

    if cardTotal > 21:
        return 999
    else:
        return cardTotal


def whoWins(player,dealer):
    if player > dealer and player < 22:
        return 'Player'
    elif dealer > player and dealer <22:
        return 'Dealer'
    elif dealer == player:
        return 'Draw'

def displayPlayerHand(hand):
    print('\nYou are holding: \n')
    for i in hand:
        print(i.rank)
        print(i.suit + '\n')

def displayDealerHand(hand, reveal):
    if reveal == False:
        print('\nDealer is holding: \n')
        for i in hand:
            print(i.rank)
            print(i.suit + '\n')
    else:
        print('\nDealer is holding: \n')
        print(hand[0].rank)
        print(hand[0].suit + '\n')
        print('And and unknown card')

while True:
    gameOn = False
    playersGo = True
    while gameOn == False:
        response = input('Would you like to play?')
        if response[0].upper() == 'Y':
            gameOn = True

    newDeck = Card.deckShuffle()

    playerHand = [newDeck.pop(0) , newDeck.pop(0)]
    dealerHand = [newDeck.pop(0) , newDeck.pop(0)]

    while gameOn == True:

        while bust(playerHand) != 999 and response.lower() != 'stick':
            displayPlayerHand(playerHand)
            displayDealerHand(dealerHand,playersGo)
            response = input('Would you like to stick or twist?')
            if response.lower() == 'twist':
                playerHand.append(newDeck.pop(0))

        playersGo = False

        if bust(playerHand) == 999:
            print('Bust! Dealer wins!')
            break

        while bust(dealerHand) <= 17:
            if bust(dealerHand) >= bust(playerHand):
                break
            print(f'The players cards value are: {bust(playerHand)}')
            displayDealerHand(dealerHand, playersGo)
            print('The dealer twisted')
            dealerHand.append(newDeck.pop(0))
        print('The dealer is sticking')
        displayDealerHand(dealerHand,playersGo)


        playerValue = bust(playerHand)
        dealerValue = bust(dealerHand)

        if dealerValue == 999:
            print('The dealer busts!')
            print('Player wins!')
            break
        print(whoWins(playerValue,dealerValue))

        if whoWins(playerValue,dealerValue) == 'Player':
            print(f'The players score is: {playerValue}')
            print(f'The dealers score is: {dealerValue}')
            print('Player wins!\n')
            break

        elif whoWins(playerValue,dealerValue) == 'Dealer':
            print(f'The players score is: {playerValue}')
            print(f'The dealers score is: {dealerValue}')
            print('Dealer wins!')
            break
        elif whoWins(playerValue,dealerValue) == 'Draw':
            print(f'It was a draw! with a score of {playerValue}')
            break


