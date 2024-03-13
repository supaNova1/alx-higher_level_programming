#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        store = i
        if (i % 3 == 0 and i % 5 == 0):
            store = "FizzBuzz"
        elif (i % 3 == 0):
            store = "Fizz"
        elif (i % 5 == 0):
            store = "Buzz"
        print("{}".format(store), end=' ')
