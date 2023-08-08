import sys

def main():
    num_of_lines = get_file()
    print(num_of_lines)

def get_file():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments" )
    else:
        if sys.argv[1].endswith(".py"):
            count = 0
            try:
                with open(sys.argv[1]) as file:
                    lines = file.readlines()
                    for line in lines:
                        if line.strip() and not line.strip().startswith("#"):
                            count += 1

            except FileNotFoundError:
                sys.exit("File does not exits")
            return count

        else:
            sys.exit("Not a Python file")


if __name__ == "__main__":
    main()


