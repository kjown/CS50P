def main():
    face = input("")
    convert(face)

def convert(face):
    emojis = [(":)", "🙂"), (":(", "🙁")]
    for emoji in emojis:
        old, new = emoji
        face = face.replace(old, new)
        print(face)

if __name__ == "__main__":
    main()

