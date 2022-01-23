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
        """
        self.value = random.randint(1, 13)

        if choice == "higher":
            self.points = 100 if self.value > current_card else 0 if self.value == current_card else -75

        elif choice == "lower":
            self.points = 100 if self.value < current_card else 0 if self.value == current_card else -75
