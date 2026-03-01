def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI (Body Mass Index) values from given heights and weights.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List of calculated BMI values.
                           Returns an empty list if an error occurs.
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Height and weight must be lists.")

        if len(height) != len(weight):
            raise ValueError(
                "Height and weight lists must have the same length.")

        bmi = []

        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) \
               or not isinstance(w, (int, float)):
                raise TypeError("All elements must be integers or floats.")

            if h == 0 or w == 0:
                raise ValueError("Height or weight cannot be zero.")

            bmi_value = w / (h ** 2)
            bmi.append(bmi_value)

        return bmi

    except Exception as error:
        print("An error occurred:", error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if BMI values is above a given limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): BMI limit.

    Returns:
        list[bool]: List of boolian values
                    (True when above a limit, False otherwise).
                    Returns an empty list if an error occurs.
    """
    try:
        if not isinstance(bmi, list):
            raise TypeError("BMI values must be a list.")

        if not isinstance(limit, int):
            raise TypeError("Limit must be an integer.")

        if not bmi:
            raise ValueError("BMI list is empty.")

        result = []

        for value in bmi:
            if not isinstance(value, (int, float)):
                raise TypeError("All BMI values must be integers or floats.")

            result.append(value > limit)

        return result

    except Exception as error:
        print("An error occurred:", error)
        return []
