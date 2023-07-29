import time


def check_pipe(file):
    with open(file, "r") as io_file:
        file_contents = io_file.read()
        if file_contents == "request":
            io_file.close()
            return True


def convert_string(file):
    with open(file, "r") as io_file:
        # Read file
        str_input = io_file.read()
        # Replace spaces and apostrophes with URL encoding chars
        new_str = str_input.replace(" ", "_").replace("'", "%27")
        # Generate url
        url = f"https://en.wikipedia.org/wiki/{new_str}"
        io_file.close()
        return url


def write_url(file):
    url = convert_string(file)
    # Write completed url back to the file
    with open(file, "w") as revised_file:
        revised_file.write(url)
        revised_file.close()


def main():
    # Pipe Check
    while True:
        if check_pipe("IO.txt"):
            convert_string("IO.txt")
            time.sleep(3)
            write_url("IO.txt")
        else:
            time.sleep(1)
            print("Checking pipe again...")


if __name__ == '__main__':
    main()

