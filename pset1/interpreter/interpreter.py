def main():
    exp = input("Expression: ")
    print(f"{calc(exp):.1f}")

def calc(exp):
    x, y ,z = exp.split(" ")
    x = float(x)
    z = float(z)
    if y == "/":
        if z == "0":
            return("ZeroDivisionError")
        else:
            return(x / z)

    elif y == "+":
        return(x + z)

    elif y == "-":
        return(x - z)

    elif y == "*":
        return(x * z)

    else:
        return("Invalid operator")

if __name__ == "__main__":
    main()



