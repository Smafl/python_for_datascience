class calculator:
    """
    A class that performs arithmetic operations between a vector and a scalar.

    Attributes:
        vector (list[int | float]): A list of integers or floats.
    """
    def __init__(self, vector: list[int | float]):
        """
        Initialize a calculator object.

        Parameters:
            vector (list[int | float]): A list of integers or floats.
        """
        self.vector = vector

    def __add__(self, scalar: int | float) -> None:
        """
        Add a scalar to a vector.

        Parameters:
            scalar (int | float): A scalar value.
        """
        print([x + scalar for x in self.vector])

    def __mul__(self, scalar: int | float) -> None:
        """
        Multiply a vector by a scalar.

        Parameters:
            scalar (int | float): A scalar value.
        """
        print([x * scalar for x in self.vector])

    def __sub__(self, scalar: int | float) -> None:
        """
        Subtract a scalar from the vector.

        Parameters:
            scalar (int | float): A scalar value.
        """
        print([x - scalar for x in self.vector])

    def __truediv__(self, scalar: int | float) -> None:
        """
        Divide a vector by a scalar.

        Parameters:
            scalar (int | float): A scalar value.
        """
        try:
            if scalar == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            print([x / scalar for x in self.vector])
        except Exception as error:
            print(ZeroDivisionError.__name__ + ":", error)
