due = 50
coins = [5, 10, 25]

def main():
    check(due, coins)

def check(due, coins):
    while due > 0:
        print("Amount Due: " + str(due))
        coin = int(input("Insert Coin: "))
        if  coin not in coins:
            print("Amount Due: " + str(due))
            coin = int(input("Insert Coin: "))
        else:
            due -= coin
    print("Change Owed: " + str(abs(due)))


main()