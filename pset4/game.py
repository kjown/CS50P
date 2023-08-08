import random

def main():
    # Assign int to be guessed
    random_num = get_level()
    guess = None
    # Check whether guess matches int
    while guess != random_num:
            guess = get_guess(random_num)
            if guess < random_num:
                print("Too small!")
            if guess > random_num:
                print("Too large!")
    print("Just right!")

# Prompt user to enter level, n
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            # If n is -ve, prompt for input again
            while n < 0:
                n = int(input("Level: "))
            # Return a int to be guessed
            return random.randint(1, n)
        # If input is not int, prompt again
        except ValueError:
            pass

# Prompt user to input their guess
def get_guess(random_num):
    while True:
        try:
            return int(input("Guess: "))
        except ValueError:
            return get_guess(random_num)

if __name__ == "__main__":
    main()