def main():
    final_fuel = get_percent()
    percent_fuel = round(final_fuel * 100)
    if percent_fuel <= 1:
        print("E")
    elif percent_fuel >= 99:
        print("F")
    else:
        print(f"{percent_fuel}%")

def get_percent():
    while True:
        #get user input
        fraction = input("Fraction: ")
        #split the input into fractions
        try:
            x, y = fraction.split("/")
            #convert fractions x and y into int
            x = int(x)
            y = int(y)
            #calculate fuel in fraction form
            fuel = x/y
            if fuel < 1:
                return fuel
        #catch errors
        except (ValueError, ZeroDivisionError):
            pass

main()



