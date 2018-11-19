import random
POINTS = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Card:
    '''Card class is made up of one element in POINTS.
    This class can return the
    value of the score and also return a
    printable string representation of a card.'''

    def __init__(self, score):
        '''score refers to an element in POINTS.
        If the value exists in POINTS, initialize it.
        Else, print "Invalid card: 'score'"'''
        if(score in POINTS):
            self.score = score
        else:
            self.score = None
            print("Invalid card: ", score)

    def get_score(self):
        '''Returns the value of this card's score'''
        return self.score

    def __str__(self):
        '''Returns printable string representation of the card'''
        return str(self.score)


class Hand:
    '''Hand class is made up of a list of cards.
    This class is capable of adding
    a card, returning the total value of the
    hand, checking if the player has a bust, and
    returning a printable representation
    of a hand.'''
    playerBust = False
    turn = 'Player 1'
    move = "n"

    def __init__(self):
        '''List of cards'''
        self.hand = []

    ## Somr desc.
    ## @param card Representation of player.
    def add_card(self, card):
        '''Add card to the list'''
        self.hand.append(card)

    def player_move(self, move):
        self.move = move
    def get_player_move(self):
        return self.move

    def get_pointvalue(self):
        '''Returns the value of a hand'''
        pointvalue = 0
        ace_exist = False
        temp = []
        for card1 in self.hand:
            temp.append(card1.get_score())

        last_card = temp[-1:]
        if last_card == 'A':
            del temp[-1]
            for p in temp:
                pointvalue += POINTS[p]
                if p == 'A':
                    ace_exist = True
            if pointvalue < 10 and ace_exist:
                pointvalue = pointvalue + 1
        else:
            for p in temp:
                pointvalue += POINTS[p]
        return pointvalue

    def print_cards(self):
        '''Return cards of both players'''
        for i in range(0, (len(self.hand))):
            print(self.hand[i], end=' ')
        print()

    def bust(self, otherplayer):
        ''' Check if the player's hand exceeds 21 (bust)'''
        # If the player has a bust, proceed according to player
        if self.get_pointvalue() > 21:
            playerBust = True
            print("{}: you have exceeded the total of 21. You're busted! {} wins!".format(self, otherplayer))
            # Print Player 1's hand and total
            print("{}'s Hand: ".format(self), self)
            print("{}'s Hand total: ".format(self), self.get_pointvalue())
            # Print Player 2's hand and total
            print("{}'s Hand: ".format(otherplayer), otherplayer)
            print("{}'s Hand total: ".format(otherplayer), otherplayer.get_pointvalue())
            return True
        return False
    # Returns printable string representation of the hand
    def __str__(self):
        cards = ''
        for card in self.hand:
            cards += str(card) + " "
        return cards.strip()


class Deck:
    '''Deck consists of a list of cards.
    This class deals a card to a hand,
    shuffls the deck, and returns a printable string
    representation of a deck'''

    def __init__(self):
        '''deck refers to a list of cards.'''
        self.deck = []
        for i in range(4):
            for score in POINTS:
                self.deck.append(Card(score))

    def deal(self):
        '''Deal a single card while removing it
        from the deck.'''
        return self.deck.pop()

    def shuffle(self):
        ''' Shuffle the deck.'''
        random.shuffle(self.deck)

    def __str__(self):
        ''' Returns printable string representation of the deck.'''
        cards = ''
        for card in self.deck:
            cards += str(card) + " "
        return cards.strip()
class UI:
    '''UI class deals with the text outputted to the player.
        Giving directions and information neccesary on the required inputs'''
    #deck = Deck()
    def playerTurn(self, player, playerHand, deck):
        '''This function takes in the player their hand.
         It facilitates the logic of a single turn
        in Blackjack'''

        # Print whose turn it is
        print('Turn: ' + player)

        # Ask the player if they want to hit or stay and proceed accordingly
        hitOrStay = input(player + ": Would you like to hit or stay? In order to receive another card type 'h', otherwise type 's' to stop taking cards.\
                          \n")

        # User input check
        while hitOrStay.lower() != 'h' and hitOrStay.lower() != 's':
            hitOrStay = input(player + ": Please type 'h' or 's' to continue.\n")

        if hitOrStay.lower() == 'h':
            # Deal a card and add it to the hand
            playerHand.add_card(deck.deal())
            print("\nOne card has been added to ", player, "'s hand.", sep="")
            # Print player's face up cards
            print(player + "'s cards: ", end=' ', sep="")
            playerHand.print_cards()

        # Record if the player decides to stay
        elif hitOrStay.lower() == 's':
            playerHand.move = 's'
        return

    def checkOutcome(self, player1, player2):
        ''' Check results of the game when both players are done'''
        # Print both player's hands and values
        print("Player 1 Hand: ", player1)
        print("Player 1 Hand Total: ", player1.get_pointvalue())
        print()
        print("Player 2 Hand: ", player2)
        print("Player 2 Hand Total: ", player2.get_pointvalue())

        # Print outcome if there is a tie or a winner
        if player1.get_pointvalue() == player2.get_pointvalue():
            print("Both players have ", player1.get_pointvalue(), "! There is a tie!",
                  sep='')
        elif player1.get_pointvalue() == 21:
            print("Player 1 has Blackjack! Player 1 wins!")
        elif player2.get_pointvalue() == 21:
            print("Player 2 has Blackjack! Player 2 wins!")
        else:
            print("\n***Player 1 Wins!***" if player1.get_pointvalue() >
                  player2.get_pointvalue() else "\n***Player 2 Wins!***")



#class testingDeck(Deck):
 #   def shuffle(self):
  #      self.deck.append(Card('A'))

class BlackJack:
    '''This class facilitates the start of the game, the player turns,
    checks the players hands as well as finishes the game'''
    player1 = Hand()
    player2 = Hand()
    deck = Deck()
    player1Stay = False
    player2Stay = False
    playerBust = False
    turn = 'Player 1'
    ui = UI()

    def main(self):

        # Shuffle the deck
        self.deck.shuffle()

        for i in range(2):
            # Deal two cards to each player's hand
            self.player1.add_card(self.deck.deal())
            self.player2.add_card(self.deck.deal())
        print("\nGame start!")
        playerbust = False
        while (not self.player1Stay or not self.player2Stay) and not self.playerBust:
            '''While either player has not "stayed" and neither player's hand is
            over 21 (bust), game continues
            Print both player's face up cards'''
            print("Player 1's cards: ", end='')
            self.player1.print_cards()
            print("Player 2's cards: ", end='')
            self.player2.print_cards()
            print()

            # Facilitate the respective player's
            # turn and check if they have a bust
            if self.turn == 'Player 1':
                self.ui.playerTurn(self.turn, self.player1, self.deck)

                if self.player1.bust(self.player2):
                    playerbust = True
                    break
            else:
                self.ui.playerTurn(self.turn, self.player2, self.deck)

                if self.player2.bust(self.player1):
                    playerbust = True
                    break

            if self.player1.move == "s" and self.player2.move == "s":
                self.ui.checkOutcome(self.player1, self.player2)
                break

            # Change turns
            if self.turn == 'Player 1' and not self.player2Stay:
                self.turn = 'Player 2'
            elif self.turn == 'Player 2' and not self.player1Stay:
                self.turn = 'Player 1'

        #if not playerbust:
            #pass
            # If both players have stayed, check the outcome to finish the game
            #self.ui.checkOutcome(player1, player2)

bj = BlackJack()
bj.main()