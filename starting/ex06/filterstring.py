import sys
from ft_filter import ft_filter


def main():
    """
    Accepts two command-line arguments:
    a string S and an integer N.

    Outputs a list of words from S that have length greater than N.

    The program uses self-implemented ft_filter() function.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        try:
            string = sys.argv[1]
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("Arguments must be a string and an integer")

        result = list(ft_filter(lambda word: len(word) > num, string.split()))
        print(result)

    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")


if __name__ == "__main__":
    main()
