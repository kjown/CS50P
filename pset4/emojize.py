# Import emoji module for use in code
import emoji

# Get user to input prompt which will convert into emoji
command = input("Input: ")

# Converts the input into emoji
command_converted = emoji.emojize(command, language ='alias')

# Outputs the converted input
print("Output: " + command_converted)

