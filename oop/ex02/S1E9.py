from abc import ABC, abstractmethod


class Character(ABC):
    """
    A class representing a character.

    Attributes:
        first_name (str): A first name of a character.
        is_alive (bool): Health state of a character.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a character object.

        Parameters:
            first_name (str): A first name of a character.
            is_alive (bool): Health state of a character.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """
        Change a character health state.
        """
        raise NotImplementedError("Die() method must be implemented.")


class Stark(Character):
    """
    A class representing a Stark family character.

    Attributes:
        first_name (str): A first name of a character.
        is_alive (bool): Health state of a character.
    """
    def die(self) -> None:
        """
        Change a character health state.
        """
        self.is_alive = False
