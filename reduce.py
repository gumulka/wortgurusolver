#!/usr/bin/python3

import os.path


def reduce():
    if not os.path.isfile("german.dic"):
        print("Please download the german dictionary \"german.dic\" from")
        print("https://sourceforge.net/projects/germandict/" +
              "files/german.7z/download")
        print("and place it inside this directory.")
        exit()
    r = open("german.dic", "r", encoding="latin-1")
    w = open("german.small", "w")

    for line in r:
        string = line.strip()
        if len(string) <= 8:
            w.write(string + "\n")


if __name__ == "__main__":
    reduce()
