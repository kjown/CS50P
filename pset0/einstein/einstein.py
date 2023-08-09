def main():
    mass = int(input("m: "))
    calculate(mass)

def calculate(mass):
    E = mass * 300000000**2
    print(E)

if __name__ == "__main__":
    main()

