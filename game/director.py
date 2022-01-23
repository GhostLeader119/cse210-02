from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.total_score = 300

        card = Card()
        self.cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:

            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        print()
        print("Thanks for playing!")

    def get_inputs(self):
        """Ask the user if they want to keep playing.

        Args:
            self (Director): An instance of Director.
        """
        draw_card = input("Play? [y/n] ")
        self.is_playing = (draw_card == "y")
        print(self.is_playing)
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your score is: {self.total_score}\n")
        if not self.is_playing:
            return 

        current_card_position = len(self.cards) - 1

        current_card = self.cards[current_card_position]

        print(f"Current card is: {current_card.value}")

        choice = input("Is the next card higher or lower? [higher/lower] ")

        new_card = Card()
        new_card.draw(current_card.value, choice)

        self.cards.append(new_card)

        self.new_card = new_card.value
        self.total_score += new_card.points

    def do_outputs(self):
        """Displays the card and the score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"The new card drawn was: {self.new_card}")
        print(f"Your score is: {self.total_score}\n")
        if self.total_score > 0:
            self.is_playing = True
        else:
            self.is_playing = False
        print(self.is_playing)
