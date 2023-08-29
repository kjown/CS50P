import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\ ?([0-5][0-9])? (AM|PM)"
    if match := re.search(r"^" + regex + " to " + regex + "$", s):
        time1 = standardize(match.group(1), match.group(2), match.group(3))
        time2 = standardize(match.group(4), match.group(5), match.group(6))
        return f"{time1} to {time2}"
    else:
        raise ValueError

def standardize(hr, min, x):
    if hr == "12":
        if x == "AM":
            hr = "00"
        else:
            hr = "12"
    else:
        if x == "AM":
            hr = f"{int(hr):02}"
        else:
            hr = f"{int(hr)+12}"
    if min == None:
        min = "00"
    else:
        min = f"{int(min):02}"
    return f"{hr}:{min}"

if __name__ == "__main__":
    main()