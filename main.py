import time


def main():
    with open("IO.txt", "w") as io_file:
        io_file.write("United states women's national soccer team")
        io_file.close()

    time.sleep(7)
    with open("IO.txt", "r") as rev_file:
        url = rev_file.read()
        rev_file.close()
        print(url)


if __name__ == '__main__':
    main()

