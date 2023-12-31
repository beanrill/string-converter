# String Converter Microservice

## About
This microservice is a string converter which takes a string and replaces any spaces with underscores `_` and any 
apostrophes with its URL encoding `%27`, then convert the modified string into a Wikipedia URL.

The microservice uses a txt file `IO.txt` as the pipe. 

## Sample Request and Receive Call

In the `main()` function of the program, "request" will be written into the pipe `IO.txt` to indicate to the 
microservice that it has received a request call. It follows with the string to be converted, also written into the pipe.
If the microservice does not receive the request call, it will continue to check by printing `Checking pipe...` on the console.

```python
with open("IO.txt", "w") as io_file:
    io_file.write("request")
    io_file.close()
    
with open("IO.txt", "w") as io_file:
    # Hard coded for this example only
    io_file.write("Spongebob Squarepants") # Hard coded for this example only
    io_file.close()
```

The microservice gets initiated once reading "request" received on the pipe, then will proceed to read the string and 
convert it into the right format for the Wikipedia URL.

**Example Conversion:**

**1) "Oregon State University"**

**2) "Oregon_State_University"**

**3) "https://en.wikipedia.org/wiki/Oregon_State_University"**

It will then write the Wikipedia URL back to the pipe, which the program then receives back.

```python
with open("IO.txt", "r") as rev_file:
    url = rev_file.read()
    rev_file.close()
    print(url)
```

## UML Sequence Diagram
![microservice_sequence_diagram.png](microservice_sequence_diagram.png)
