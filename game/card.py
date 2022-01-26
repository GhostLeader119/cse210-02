try:
    import random


    class Card:
        """A card with a different value.

        The responsibility of Card is to keep track of the side value of the card and calculate the points for 
        it.
    
        Attributes:
            value (int): The number on the card.
        """

        def __init__(self):
            """Constructs a new instance of Card.

            Args:
                self (Card): An instance of Card.
            """
            self.value = random.randint(1, 13)
            self.points = 0

        def draw(self, current_card, choice):
            """Generates a new random value and calculates the points for the Card.
            
            Args:
                self (Card): An instance of Card.
                current_card: The first card drawn in the round
                choice: user input, the players guess
            """
            self.value = random.randint(1, 13)

            if choice == "higher":
                self.points = 100 if self.value > current_card else 0 if self.value == current_card else -75

            elif choice == "lower":
                self.points = 100 if self.value < current_card else 0 if self.value == current_card else -75

except ModuleNotFoundError:
    #informs user of an error and trys to log it
    print('\nError: Critical files not found or corrupted...\nFailed to find [random]\n')
    try:
        from error_logger import Error_logger
        ident = 'ModuleNotFoundError [random] @ card.py'
        log_master = Error_logger()
        log_master.scribe(ident)
    except ModuleNotFoundError:
        print('Could not log error: File missing')
except ImportError:
    #informs user of an error and trys to log it
    print('\nError: Class or variable could not be retrieved from card.py...\n')
    try:
        from error_logger import Error_logger
        ident = 'ImportError @ card.py'
        log_master = Error_logger()
        log_master.scribe(ident)
    except ModuleNotFoundError:
        print('Could not log error: File missing')
