class calculator:
    """
    A class that performs arithmetic operations between two vectors.
    Consist only static methods.
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate a dot product of two vectors.

        Parameters:
            V1 (list[float]): A list of floats.
            V2 (list[float]): A list of floats.
        """
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors.

        Parameters:
            V1 (list[float]): A list of floats.
            V2 (list[float]): A list of floats.
        """
        result = [a + b for a, b in zip(V1, V2)]
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract two vectors.

        Parameters:
            V1 (list[float]): A list of floats.
            V2 (list[float]): A list of floats.
        """
        result = [a - b for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
