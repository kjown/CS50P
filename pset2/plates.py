def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #vanity plates may contan a max of 6 char and a minimum of 2 chars
    if len(s) < 2 or len(s) > 6:
        return False

    #All vanity plates must start with at least two letters
    for c in s[:2]:
        if not c.isalpha():
            return False

    #Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i:].isdigit() == False:
                return False

    #The first number used cannot be a ‘0’.
    for i in s:
        if i.isdigit():
            if int(i)==0:
                return False
            else:
                break

    #“No periods, spaces, or punctuation marks are allowed.”
    for c in s:
        if c in [".", " ", "!", "?", ",", "'", '"']:
            return False

    #If all test pass, return True
    return True

main()