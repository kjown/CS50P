def main():
    greeting = str(input("Greeting: "))
    amount = value(greeting.lower().strip())
    print(f"${amount}")

def value(greeting):
    if "hello" in greeting:
        value = 0
    else:
        if greeting.startswith("h"):
            value = 20
        else:
            value = 100
    return value

if __name__ == "__main__":
    main()