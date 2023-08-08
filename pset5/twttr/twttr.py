def main():
    word = str(input("Input: "))
    print(shorten(word))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    for letter in word:
        # Correct line
         if letter.lower() in vowels:
        # Create bug of not catching uppercase letters
        #if letter in vowels:
            word =  word.replace(letter, "")
    return word

if __name__ == "__main__":
    main()