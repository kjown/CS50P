# make a dictionary
dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# with a while loop prompt for item and add item value until user input exit
total = 0
while True:
    try:
        item = input("Item: ").strip().title()
        for order in dict:
            if order == item:
                total = total + (dict[order])
                print(f"${total}")
    except EOFError:
        break