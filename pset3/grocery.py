#create a dictionary
grocery = {}

#repeatly prompt user for input until conrtrol-d is inputted
while True:
    try:
        #get user input
        item = input().lower()
        #check if item is in grocery
        if item in grocery:
            #if in grocery, add 1 count
            grocery[item] += 1
        #otherwise, add item for first time
        else:
            grocery[item] = 1
    except EOFError:
        #print all items in alphabetical order
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        #stop the loop
        break