import csv
import sys

def main():
    students = read()
    write(students)

def read():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            try:
                student_list = []

                with open(sys.argv[1]) as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        student_list.append({"name": row["name"], "house": row["house"]})
                return student_list

            except FileNotFoundError:
                sys.exit(f"Could not read {sys.argv[1]}")

        else:
            sys.exit("Not a CSV file")


def write(students):
    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for student in students:
            last, first = student["name"].split(", ")
            house = student["house"]
            writer.writerow({"first": first, "last": last, "house": house})



if __name__ == "__main__":
    main()

