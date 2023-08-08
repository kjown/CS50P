from PIL import Image, ImageOps
import sys
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        inp = os.path.splitext(sys.argv[1])
        output = os.path.splitext(sys.argv[2])
        ext = [".jpg", ".jpeg", ".png"]

        if inp[1] in ext and output[1] in ext:
            try:
                if inp[1] == output[1]:
                    overlay_shirt(sys.argv[1], sys.argv[2])
                else:
                    sys.exit("Input and output have different extensions")

            except FileNotFoundError:
                sys.exit("Input does not exist")
        else:
            if inp[1] not in ext:
                sys.exit("Invalid input")
            elif inp[2] not in ext:
                sys.exit("Invalid output")
            elif inp[1] not in ext and output[1] not in ext:
                sys.exit("Invalid input and output")

def overlay_shirt(input_image, output_image):
    shirt =  Image.open("shirt.png")
    with Image.open(sys.argv[1]) as input_image:
        final_photo = ImageOps.fit(input_image, shirt.size)
        final_photo.paste(shirt, (0,0), shirt)
        final_photo.save(output_image)

if __name__ == "__main__":
    main()