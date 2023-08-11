s = input("camelCase: ")
print("snake_case: ", end="")
for c in s:
    if c.isupper() == True:
        print("_" + c.lower(), end="", sep="")
    else:
        print(c, end="")
print()
