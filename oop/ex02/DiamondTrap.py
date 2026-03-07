from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    A class representing a King character.

    Attributes:
        first_name (str): A first name of a character.
        is_alive (bool): Health state of a character.
    """
    def set_eyes(self, color: str) -> None:
        """
        Set the eyes color.

        Parameters:
            color (str): A new color.
        """
        self.eyes = color

    def set_hair(self, color: str) -> None:
        """
        Set the hair color.

        Parameters:
            color (str): A new color.
        """
        self.hair = color

    def get_eyes(self) -> str:
        """
        Get eyes color.

        Returns:
            str: Current eyes color.
        """
        return self.eyes

    def get_hair(self) -> str:
        """
        Get hair color.

        Returns:
            str: Current hair color.
        """
        return self.hair
