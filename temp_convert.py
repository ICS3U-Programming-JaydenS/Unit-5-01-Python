#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 19, 2025
# This program tells you the sum of the user's number


def fahrenheit():
    celsius = input("What is your tempature in Celsius ")
    try:
        celsius_int = float(celsius)
        if celsius_int < 0:
            fahrenheit = -1 * (celsius_int * 9 / 5 + 32)
            print(
                celsius_int,
                "degrees celsius in fahrenheit is {:.2f}".format(fahrenheit),
            )
        else:
            fahrenheit = celsius_int * 9 / 5 + 32
            print(celsius_int, "degrees celsius in fahrenheit is", (fahrenheit))
    except Exception:
        print(celsius, "is not a positive integer!")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
