#!/usr/bin/python3

def main():
    print("Hello World!")
    name = input("What is your name? ")
    greet(name)

def greet(name):
    print("Hello {}!".format(name))

if __name__ == "__main__":
    main()
