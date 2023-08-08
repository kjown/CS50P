import inflect

p = inflect.engine()

# Create a list to store the names inputted
name_list = []

# Prompts user for names, one per line, until user input ctrl-d
while True:
    try:
        name = input("Name: ")
        name_list.append(name)


    # Bid adieu to the names, seperating with comma and "and"
    except EOFError:
        print()
        break

# Display output using inflect module
names = p.join(name_list)

print("Adieu, adieu, to " + names)
