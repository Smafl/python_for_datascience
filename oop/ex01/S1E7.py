from S1E9 import Character


class Baratheon(Character):
    """
    A class represing a Baratheon family character.

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
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

    def die(self):
        """
        Change a character health state.
        """
        self.is_alive = False

    def __str__(self):
        return (
            f"{self.__class__.__name__}:"
            f"{self.family_name}, {self.eyes}, {self.hair}"
        )

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    """
    A class represing a Lannister family character.

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
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hair = "light"

    def die(self):
        """
        Change a character health state.
        """
        self.is_alive = False

    def __str__(self):
        return (
            f"{self.__class__.__name__}:"
            f"{self.family_name}, {self.eyes}, {self.hair}"
        )

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        return cls(first_name=first_name, is_alive=is_alive)
