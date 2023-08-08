fruits = {
    "apple" : "130",
    "avocado" : "50",
    "banana" : "110"

}

item = input("Item: ")
if item.lower() in fruits:
    print(fruits[item])

