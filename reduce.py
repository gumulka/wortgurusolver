#!/usr/bin/python3


def reduce():
    r = open("german.dic", "r", encoding="latin-1")
    w = open("german.small", "w")

    for line in r:
        string = line.strip()
        if len(string) <= 8:
            w.write(string + "\n")


if __name__ == "__main__":
    reduce()
