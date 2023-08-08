import random

def main():
    level = get_level()
    score = 0
    # Generate 10 maths problems
    for i in range(10):
        x, y = generate_integer(level), generate_integer(level)
        tries = 1
        ans = int(input(f"{x} + {y} = "))
        if ans == x+y:
            score += 1
        else:
            # If no. of tries is not 3, prompt for answer again
            while tries != 3:
                tries += 1
                print("EEE")
                ans = int(input(f"{x} + {y} = "))
                if ans == x +y:
                    score += 1
                    break
            # If no. of tries is 3, print the answer
            if tries == 3:
                print(f"{x} + {y} = {x+y}")
    # Display the total score obtained
    print(f"Score: {score}")

# Prompt user for level, n
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            # If user does not input 1, 2, 3, reprompt
            if n in [1, 2, 3]:
                return n
            else:
                continue
        # If non-int is entered, reprompt
        except ValueError:
            continue

# Randomly generate 10 math problems in "X + Y =" format, where X and Y are +ve
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()