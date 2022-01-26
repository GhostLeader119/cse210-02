import random


class card_generator:
    """ The card generator will produce a randome card from 1 to 13 that 
    will be used for the game.

    Attributes:
    self.card sets the card value"""
    # generates a card to be used at call point, returns INT

    def __init__(self):
        """ Constructs a new instance of car_generator."""
        # sets default card value
        self.card = 0

    def draw(self):
        """Method/Function:   
        This will generate a card from 1 to 13"""
        # randomly draws a card with values between 1 to 13
        self.card = random.randint(1, 13)
        return self.card


class game_master:
    """game_master is going to direct the game and control the sequence of the play.

    Attibutes:
    List = self.card = [] : this will create a list from the card_generator and hold the values
    Boolean = self.is_playing = True : This is saying the game will continue till the user says (n or NO)
    Int = self.score = 300 : This is the amount you start off with, based on user input the anount will either increase or decrease
    Boolean = self.playerchoice = None : This will hold false till the user inputs a choice."""

    def __init__(self):
        """Constructs a new director"""
        # sets default values
        self.cards = []
        self.is_playing = True
        self.score = 300
        self.playerchoice = None

    def draw_cards(self):
        """Method/Function:
         Draws two (2) cards and place them in the self.cards list

          Args:
        self (game_master): An instance of game_master"""
        # draws the cards set to be used for the round, calls card_generator class
        for i in range(2):
            card_gen = card_generator()
            card = card_gen.draw()

            self.cards.append(card)

    def start_game(self):
        """Method/Function:
        Starts running the game and will continue till the user answer no (N) to continue.

         Args:
        self (game_master): An instance of game_master"""
        # central control function/switchboard
        while self.is_playing:
            self.draw_cards()
            self.display_card()
            self.get_inputs()
            self.display_card()
            self.do_updates()
            self.do_result()

    def display_card(self):
        """Method/Function:
        This is display the first card and then display the card that the user was guessing to be high or low.

         Args:
        self (game_master): An instance of game_master"""
        # displays the cards
        card_1 = self.cards[0]
        card_2 = self.cards[1]

        if self.playerchoice == None:
            print(f'Card 1: {card_1}')
        else:
            print(f'\nCard 2: {card_2}')

    def get_inputs(self):
        """Method/Function:
        Asks the user if the card that is not displayed yet is HI or LOW

        Args:
        self (game_master): An instance of game_master"""
        # gets user inputs
        while True:
            choice = input('Will the next card be [HI] or [LOW]: ').upper()

            if choice == 'HI' or choice == 'LOW':
                self.playerchoice = choice
                break
            else:
                print('Invalid input...')

    def do_updates(self):
        """Method/Function:
        Analyzes if car_1 is greater than or lesser than card_2
        and updates score based on the users choice of HI or LOW and will display 
        a message and display the current score..

         Args:
        self (game_master): An instance of game_master"""
        # analyzes score using player input
        card_1 = int(self.cards[0])
        card_2 = int(self.cards[1])

        if card_1 < card_2:
            analyze = 'HI'
        elif card_1 > card_2:
            analyze = 'LOW'
        else:
            analyze = 'the same'

        # determines points
        translation = self.playerchoice
        if analyze == translation:
            print('You guessed correct!')
            self.score += 100
        else:
            print('You guessed wrong!')
            self.score -= 75

        print(f'Current score: {self.score}')
        # Reset playerchoice for display_card()
        self.playerchoice = None

    def do_result(self):
        """Method/Function:
        Will display the game is over if user has run out point and end the game.

         Args:
        self (game_master): An instance of game_master
        """
        # calculate results and see if game is over
        self.cards = []  # resets cards for next round if necesary
        if self.score < 1:
            # ends game if points run out
            print('\nGAME OVER!\nYou are out of points!')
            self.is_playing = False
            return

        choice = input('\nWould you like to continue? Y/N ').upper()
        if choice == 'N' or choice == 'NO':
            self.is_playing = False
            return
        elif choice == 'Y' or choice == 'YES':
            return
        else:
            print('invalid input...')


program_status = game_master()
program_status.start_game()
