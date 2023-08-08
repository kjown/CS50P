s = input("camelCase: ")
print("snake_case: ", end="")
for c in s:
    if c.isupper() == True:
        print("_" + c.lower(), end="")
    else:
        print(c, end="" )
