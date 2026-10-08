def count_text(file):
    try:
        l = w = c = 0

        with open(file, "r") as f:
            for i in f:
                l += 1
                w += len(i.split())
                c += len(i)

        print("Lines:", l)
        print("Words:", w)
        print("Characters:", c)

    except FileNotFoundError:
        print("The file does not exist.")
    except Exception:
        print("Unable to read the file.")


name = input("File name: ")
count_text(name)
