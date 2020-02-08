import random
deckNumber = 4 ## Number of pack of cards you want
numberOfSims = 83863
shufflePercentage = 90


def deckShuffle(): ## Shuffles the amount of decks wanted and returns it
    deck = []
    for i in range(0, deckNumber):
        for numberofsuits in range(0, 4):
            for rank in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']:
                deck.append(rank)
    random.shuffle(deck)
    return deck

def handValue(hand):
    value = 0
    aces = 0
    for i in hand:
        if i in ['10', '9', '8', '7', '6', '5', '4', '3', '2']:
            value += int(i)
        elif i in ['K', 'Q', 'J']:
            value += 10
        else:
            value += 11
            aces += 1

    while aces > 0:
        if value > 21:
            value -= 10
            aces -= 1
        else:
            break
    return value

def reshuffle(deck):
    newDeck = deckShuffle()
    if len(deck) < ((deckNumber * 52) * (shufflePercentage / 100)):
        return newDeck
    else:
        return deck


shuffledDeck = deckShuffle()
playerWins = 0
dealerWins = 0
draws = 0
shuffleCount = 0
playerBustCount = 0
dealerBustCount = 0

### Sim starts here
for i in range(0,numberOfSims):
    playersHand = []
    dealersHand = []
    sizeCheck = len(shuffledDeck)
    shuffledDeck = reshuffle(shuffledDeck)
    if sizeCheck < len(shuffledDeck):
        shuffleCount += 1

    ## Deals the cards to the players
    playersHand = [shuffledDeck.pop(0)]
    dealersHand = [shuffledDeck.pop(0)]
    playersHand += [shuffledDeck.pop(0)]
    dealersHand += [shuffledDeck.pop(0)]

    while handValue(playersHand) < 12:
        playersHand += shuffledDeck.pop(0)

    playersHandValue = handValue(playersHand)

    if playersHandValue >21:
        dealerWins += 1
        playerBustCount += 1
        continue

    elif playersHandValue == 21:
        playerWins += 1
        continue

    while handValue(dealersHand) <= 17:
        dealersHand += shuffledDeck.pop(0)

    dealersHandValue = handValue(dealersHand)

    if dealersHandValue > 21:
        playerWins += 1
        dealerBustCount += 1
        continue
    if playersHandValue > dealersHandValue:
        playerWins += 1
    elif dealersHandValue > playersHandValue:
        dealerWins += 1
    elif playersHandValue == dealersHandValue:
        draws += 1

print(f'\nThe number of player victories: {playerWins}  {round((playerWins / numberOfSims) * 100,2)}%')
print(f'The number of dealer victories: {dealerWins}  {round((dealerWins / numberOfSims) * 100,2)}%')
print(f'The number of draws: {draws}  {round((draws / numberOfSims) * 100,2)}%')
print(f'The deck was shuffled {shuffleCount} times!\n')
print(f'The dealer went bust {dealerBustCount} times!, the player went bust {playerBustCount} times!')