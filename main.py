import time


def main():
    # Initiate a request
    with open("IO.txt", "w") as io_file:
        io_file.write("request")
        io_file.close()
    time.sleep(1)
    with open("IO.txt", "w") as io_file:
        # Hard coded for this example only
        io_file.write("Spongebob Squarepants")
        io_file.close()
    time.sleep(5)
    with open("IO.txt", "r") as rev_file:
        url = rev_file.read()
        rev_file.close()
        print(url)


if __name__ == '__main__':
    main()

