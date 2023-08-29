import re
import sys

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        sys.exit("True")
    else:
        sys.exit("False")

def validate(ip):
    if ip := re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        groups = [int(group) for group in ip.groups()]
        for group in groups:
            if not (0 <= group <= 255):
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()