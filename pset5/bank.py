def main():
    greeting = str(input("Greeting: "))
    amount = value(greeting)
    print(f"${amount}")

def value(greeting):
    if "hello" in greeting.lower().strip():
        value = 0
    elif greeting[0] == "h":
        value = 20
    else:
        value = 100
    return value

if __name__ == "__main__":
    main()