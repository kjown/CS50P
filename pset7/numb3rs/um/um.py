import re

def main():
    print(count(input("Text: ")))

def count(s):
    result = len(re.findall(r"\bum\b", s, re.IGNORECASE))
    return result


if __name__ == "__main__":
    main()