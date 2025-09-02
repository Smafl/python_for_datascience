import sys

def main():
    try:
        if len(sys.argv) == 1:
            return

        assert len(sys.argv) == 2, "more than one argument is provided"

        try:
            arg = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        if arg % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")

if __name__ == "__main__":
    main()
