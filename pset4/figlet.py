import random
import sys
from pyfiglet import Figlet

figlet = Figlet()



# Get a list of available fonts
figlet.getFonts()

# Check whether argument is zero or two command-line
try:
    # If ZERO, output random font
    if len(sys.argv) == 1:
        f = random.choice(figlet.getFonts())
        figlet.setFont(font=f)

    # If TWO, check whether first command-line is "-f" or "--font"
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f") or (sys.argv[1] == "--font"):
        # If TRUE, check second command-line for name of font
        figlet.setFont(font=(sys.argv[2]))

    # If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
    else:
        sys.exit("Invalid usage")

except:
    sys.exit("Invalid usage")

# Prompt user for a str of text
s = input("Input: ")

# Outputs text in desired font
print(figlet.renderText(s))