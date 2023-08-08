text = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]

for letter in text:
    if letter.lower() in vowels:
        text = text.replace(letter, "")

print("Output: " + text)





