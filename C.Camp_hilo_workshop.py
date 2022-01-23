import random

class card_generator:
    # generates a card to be used at call point, returns INT
    def __init__(self):
        #sets default card value
        self.card = 0

    def draw(self):
        #randomly draws a card with values between 1 to 13
        self.card = random.randint(1, 13)
        return self.card

class game_master:

    def __init__(self):
        # sets default values
        self.cards = []
        self.is_playing = True
        self.score = 300
        self.playerchoice = None

    def draw_cards(self):
        for i in range(2):
            card_gen = card_generator()
            card = card_gen.draw()

            self.cards.append(card)
    
    def start_game(self):
        #central control function
        while self.is_playing:
            self.draw_cards()
            self.display_card()
            self.get_inputs()
            self.display_card()
            self.do_updates()
            self.do_result()
    
    def display_card(self):
        #displays the cards
        card_1 = self.cards[0]
        card_2 = self.cards[1]

        if self.playerchoice == None:
            print(f'Card 1: {card_1}')
        else:
            print(f'\nCard 2: {card_2}')


    def get_inputs(self):
        #gets user inputs
        while True:
            choice = input('Will the next card be [HI] or [LOW]: ').upper()
            
            if choice == 'HI' or choice == 'LOW':
                self.playerchoice = choice
                break
            else:
                print('Invalid input...')

    def do_updates(self):
        #analyzes score using player input
        card_1 = int(self.cards[0])
        card_2 = int(self.cards[1])

        if card_1 < card_2:
            analyze = 'HI'
        elif card_1 > card_2:
            analyze = 'LOW'
        else:
            analyze = 'the same'

        translation = self.playerchoice
        if analyze == translation:
            print('You guessed correct!')
            self.score += 100
        else:
            print('You guessed wrong!')
            self.score -= 75

        print(f'Current score: {self.score}')
        #Reset playerchoice for display_card()
        self.playerchoice = None

    def do_result(self):
        #calculate results and see if game is over
        self.cards = []
        if self.score < 1:
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
