# import necessary packages etc
from enum import IntEnum
from random import randint

# Card class to represent a card
class Card(object):
    # we create an IntEnum to represent the different suits. This is essentially an integer data type that can be
    # in one of five states, MAX_SUIT is useful as it is the number of suits and can be used as the upper bound
    # in any indexing
    class Suit(IntEnum):
        HEART = 0
        DIAMOND = 1
        CLUB = 2
        SPADE = 3
        MAX_SUIT = 4
    # IntEnum as above but for the rank of the cards
    class Rank(IntEnum):
        TWO = 0
        THREE = 1
        FOUR = 2
        FIVE = 3
        SIX = 4
        SEVEN = 5
        EIGHT = 6
        NINE = 7
        TEN = 8
        JACK = 9
        QUEEN = 10
        KING = 11
        ACE = 12
        MAX_RANK = 13
    # constructor to initialise the rank and suit of the card instance
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    # method to return the value of the card as an integer utilizing a switch function and the above enumerations
    # (ace = 11)
    def getCardValue(self):

        if   (self.rank == Card.Rank.TWO):   return 2
        elif (self.rank == Card.Rank.THREE): return 3
        elif (self.rank == Card.Rank.FOUR):  return 4
        elif (self.rank == Card.Rank.FIVE):  return 7
        elif (self.rank == Card.Rank.SIX):   return 6
        elif (self.rank == Card.Rank.SEVEN): return 7
        elif (self.rank == Card.Rank.EIGHT): return 8
        elif (self.rank == Card.Rank.NINE):  return 9
        elif (self.rank == Card.Rank.TEN):   return 10
        elif (self.rank == Card.Rank.JACK):  return 10
        elif (self.rank == Card.Rank.QUEEN): return 10
        elif (self.rank == Card.Rank.KING):  return 10
        elif (self.rank == Card.Rank.ACE):   return 11
        else:                                return 0
    # overload the str() operator to return an string XY where X is the rank and Y is the suit of the card
    def __str__(self):
        card = ""
        if   (self.rank == Card.Rank.TWO):   card += "2"
        elif (self.rank == Card.Rank.THREE): card += "3"
        elif (self.rank == Card.Rank.FOUR):  card += "4"
        elif (self.rank == Card.Rank.FIVE):  card += "5"
        elif (self.rank == Card.Rank.SIX):   card += "6"
        elif (self.rank == Card.Rank.SEVEN): card += "7"
        elif (self.rank == Card.Rank.EIGHT): card += "8"
        elif (self.rank == Card.Rank.NINE):  card += "9"
        elif (self.rank == Card.Rank.TEN):   card += "10"
        elif (self.rank == Card.Rank.JACK):  card += "J"
        elif (self.rank == Card.Rank.QUEEN): card += "Q"
        elif (self.rank == Card.Rank.KING):  card += "K"
        elif (self.rank == Card.Rank.ACE):   card += "A"
        else:                                card += "?"

        if   (self.suit == Card.Suit.HEART):   card += "H"
        elif (self.suit == Card.Suit.CLUB):    card += "C"
        elif (self.suit == Card.Suit.DIAMOND): card += "D"
        elif (self.suit == Card.Suit.SPADE):   card += "S"
        else:                                  card += "?"

        return card
    # method to print the str() conversion of the card
    def print(self):
        print(str(self),end='')

# Deck class to represent a deck of cards
class Deck(object):
    def __init__(self):
        # Deck will have as a member variable a list of cards which we initially construct in order
        cardList = []
        for suit in range(0,Card.Suit.MAX_SUIT):
            for rank in range(0,Card.Rank.MAX_RANK):
                cardList.append(Card(rank,suit))
        self.cardList =cardList
        # Deck has a member variable called cardIndex which is the index of the card currently at the top of the deck
        # this is useful in dealing cards from the deck
        self.cardIndex = 0


    # method to shuffle the deck of cards
    def shuffleDeck(self):
        # swap each card in the deck with another randomly selected card from the deck
        for i in range(0,len(self.cardList)):
            randomCardIndex = randint(0,51)
            self.cardList[i],self.cardList[randomCardIndex] = self.cardList[randomCardIndex],self.cardList[i]
        # reset the card index to zero so that it is now pointing at the first card on the top of the deck again
        self.cardIndex = 0
    # method to print the whole deck of cards in order
    def printDeck(self):
       for card in self.cardList:
           card.print()
           print(end=' ')
       print()
    # method to deal card
    def dealCard(self):
        # increase cardIndex so it now indexes card below dealt card
        self.cardIndex += 1
        # return the card from the top, need to have cardIndex-1 since we just incremented cardIdex
        return self.cardList[self.cardIndex-1]
# function to get the choice of the player, whether to stick or twist
def getPlayerChoice():
    choice = ""
    # here we use the while loop to keep asking the user for an input until they give a correct one
    while(choice!='h' and choice!='s'):
        choice = str(input("(h) to hit  or (s) to stick: "))
    return choice

# function to actually implement the game logic, returns True/False depending on whether the player won
def playBlackjack(deck):
    # initialise player total and dealer totals to zero
    playerTotal = 0
    dealerTotal = 0

    # dealer is initially dealt one card face up and one face down; this is equivalent to being dealt only one card
    dealerTotal += deck.dealCard().getCardValue()
    print("The dealer is showing: " + str(dealerTotal))

    # player is initially dealt two cards
    playerTotal += deck.dealCard().getCardValue()
    playerTotal += deck.dealCard().getCardValue()

    # use a while(True) to keep asking the player for their action till they stick or bust
    while(True):
        # display player total
        print("You have " + str(playerTotal))
        # get player choice using are function from above
        choice = getPlayerChoice()
        # if the player sticks break out of while loop
        if(choice=='s'):
            break
        # otherwise deal a card and add to the player total it's value
        playerTotal+=deck.dealCard().getCardValue()
        # if the player exceeds 21 they are bust
        if(playerTotal>21):
            # tell the player how bust they were and return False so that they lost
            print(str(playerTotal)+ " you are bust!")
            return False
    # as long as the dealer total is less than 17 we have them twist
    while(dealerTotal<17):
        dealerTotal+=deck.dealCard().getCardValue()
        # display the dealer total
        print("The dealer now has " + str(dealerTotal))
    # if the dealer goes bust the player wins by default
    if(dealerTotal>21):
        return True
    # if the player total is greater than the dealer total then the player wins, the above conditionals take cover
    # the cases when either the dealer or player is bust, so at by this point both the player and dealer have totals
    # less than or equal to 21. If both player and dealer have 21 then the dealer wins by the rules of Blackjack. This
    # is taken account of by our conditional return.
    return (playerTotal>dealerTotal)


# This is where the actual game gets played

# create a deck
deck = Deck()
# shuffle the deck
deck.shuffleDeck()
# play the Blackjack game. Here it is exucuted in the if statement since it returns a bool representing whether the
# player won or lost, we then use that to print the result to the screen
if(playBlackjack(deck)):
    print("You Win!")
else:
    print("You Loose!")


