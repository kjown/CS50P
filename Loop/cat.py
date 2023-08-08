def main():
    num = get_num()
    meow(num)

def get_num():
    while True:
        n = int(input('What is n? '))
        if n > 0:
            return n

def meow(num):
    for _ in range(num):
        print("meow")

main()