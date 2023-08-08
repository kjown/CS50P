import sys
import requests
import json

def main():
    bitcoin = get_coin()
    convert(bitcoin)

def get_coin():
    # User to specify no. of Bitcoins, n
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # If argument cannot be converted to float, exit
    try:
        n = sys.argv[1]
        return float(n)
    except ValueError:
        sys.exit("Command-line argument is not a number")

def convert(bitcoin):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r = response.json()
        amount = (r["bpi"]["USD"]["rate_float"])*bitcoin
        amount = float(amount)
        print(f"${amount:,.4f}")
    except requests.RequestException:
        sys.exit("RequestException")

if __name__ == "__main__":
    main()



