text= input("Write a Letter or a Number: ")
print("The ASCII value of '" + text + "' is", ord(text))

if ord(text) > 1:
    for i in range(2, ord(text)):
        if (ord(text) % i) == 0:
            print(ord(text), "is not a prime number")
            print(i, "times", ord(text) // i, "is", ord(text))
            break
    else:
        print(ord(text), "is a prime number")
else:
    print(ord(text), "is not a prime number")