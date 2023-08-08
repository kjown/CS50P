import csv
import sys
from tabulate import tabulate

def main():
    table = get_file()
    print(table)

def get_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.reader(file)
                    table = tabulate(reader, headers="firstrow", tablefmt="grid")
                    return table
            except FileNotFoundError:
                sys.exit("File not found")
        else:
            sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()


