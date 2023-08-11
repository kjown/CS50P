images = [("gif", "gif"), ("jpg", "jpeg"), ("jpeg", "jpeg"), ("png", "png")]
app = [("pdf", "pdf"), ("zip", "zip")]
text = [("txt", "plain")]


def main():
    file = input("File name: ")
    read(file)

def read(file):
    file_split = file.lower().strip().split(".")
    if len(file_split) > 1:
        for i in images:
            if file_split[-1] in i:
                print("image/" + i[1])
                return
        for a in app:
            if file_split[-1] in a:
                print("application/" + a[1])
                return
        for t in text:
            if file_split[-1] in t:
                print("text/" + t[1])
                return


    print("application/octet-stream")

if __name__ == "__main__":
    main()



