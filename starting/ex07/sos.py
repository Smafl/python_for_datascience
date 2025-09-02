import sys


def main():
    """
    The program encodes an input string into Morse Code
    and prints the encoded string.

    Accepts at most one command-line argument.

    The program supports space and alphanumeric characters.
    Complete morse characters are separated by a single space.
    Spaces in the input are represented by a slash ("/") in the output.
    """

    # Dictionary representing the morse code chart
    MORSE_CODE_DICT = {
        ' ':  '/',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----'
    }

    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        string = sys.argv[1].upper()
        result = []
        for c in string:
            if c in MORSE_CODE_DICT:
                result.append(MORSE_CODE_DICT[c])
            else:
                raise AssertionError("the arguments are bad")

        print(" ".join(result))

    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")


if __name__ == "__main__":
    main()
