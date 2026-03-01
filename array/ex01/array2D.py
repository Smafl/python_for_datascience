import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Truncate an array based on the given start and end indices.
    Prints the original and new array shapes.

    Args:
        family (list): A 2D array.
        start (int): Index to start truncation from.
        end (int): Index to end truncation at.

    Returns:
        list: A new truncated array.
              Returns an empty list if an error occurs.
    """
    try:
        if not isinstance(family, list):
            raise TypeError("Input must be a list.")

        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Start and end must be integers.")

        if not all(isinstance(row, list) for row in family):
            raise TypeError("Input must be a 2D list")

        family_np = np.array(family)

        if family_np.ndim != 2:
            raise ValueError("Input must be a 2D list")

        new_list = np.array(family_np[start:end])

        print("My shape is : ", np.array(family).shape)
        print("My new shape is : ", new_list.shape)

        return new_list.tolist()

    except Exception as error:
        print("An error occurred:", error)
        return []
