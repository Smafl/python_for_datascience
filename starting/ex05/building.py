import sys
import string


def count_chars(input_str):
    """
    Count different categories of characters in a string.

    Categories counted:
    - total_char: total number of characters
    - uppercase: uppercase alphabetic characters (A–Z)
    - lowercase: lowercase alphabetic characters (a–z)
    - punctuation: characters from string.punctuation
    - digit: numeric characters (0–9)
    - space: whitespace characters (spaces, tabs, newlines, etc.)

    Arguments:
        input_str (str): The text to analyze.
    """

    characters = {
        "total_char": 0,
        "uppercase": 0,
        "lowercase": 0,
        "punctuation": 0,
        "digit": 0,
        "space": 0,
    }

    for char in input_str:
        characters['total_char'] += 1
        if char.isupper():
            characters["uppercase"] += 1
        elif char.islower():
            characters["lowercase"] += 1
        elif char.isdigit():
            characters["digit"] += 1
        elif char.isspace():
            characters["space"] += 1
        elif char in string.punctuation:
            characters["punctuation"] += 1

    print(
        f"The text contains {characters['total_char']} characters:\n"
        f"{characters['uppercase']} upper letters\n"
        f"{characters['lowercase']} lower letters\n"
        f"{characters['punctuation']} punctuation marks\n"
        f"{characters['space']} spaces\n"
        f"{characters['digit']} digits"
    )


def main():
    """
    Entry point of the program.

    - Accepts at most one command-line argument.
    - If a string argument is provided, analyzes it directly.
    - If no argument is given, prompts the user to enter text.
    - If more than one argument is provided, raises an AssertionError.

    The program computes character statistics
    and prints the results in a formatted summary.
    """

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        input_str = ''
        try:
            input_str = sys.argv[1]
        except IndexError:
            while not input_str:
                input_str = input("What is the text to count?\n")

        count_chars(input_str)

    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")


if __name__ == "__main__":
    main()
