import time

while True:
    time.sleep(3)
    with open("IO.txt", "r") as io_file:
        # Read file
        str_input = io_file.read()
        # Replace spaces and apostrophes to URL encoding
        new_str = str_input.replace(" ", "_").replace("'", "%27")
        # Attach to url
        url = f"https://en.wikipedia.org/wiki/{new_str}"
        io_file.close()
        time.sleep(3)
        # Write back to the file
        with open("IO.txt", "w") as revised_file:
            revised_file.write(url)
            revised_file.close()
            break



