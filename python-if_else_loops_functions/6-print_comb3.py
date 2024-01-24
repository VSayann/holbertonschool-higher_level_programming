#!/usr/bin/python3
for number in range(100):
    if number < 90:
        if number % 10 > number / 10:
            print("{:02d}, ".format(number), end="")
