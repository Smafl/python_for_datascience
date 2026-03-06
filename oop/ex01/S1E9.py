from abc import ABC, abstractmethod


class Character(ABC):
    """
    A class represing a character.

    Attributes:
        first_name (str): A first name of a character.
        is_alive (bool): Health state of a character.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a character object.

        Parameters:
            first_name (str): A first name of a character.
            is_alive (bool): Health state of a character.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Change a character health state.
        """
        raise NotImplementedError("Die() method must be implemented.")


class Stark(Character):
    """
    A class represing a Stark family character.

    Attributes:
        first_name (str): A first name of a character.
        is_alive (bool): Health state of a character.
    """
    def die(self):
        """
        Change a character health state.
        """
        self.is_alive = False
