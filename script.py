#!/usr/bin/python3

import sys

f = open("german.dic", "r", encoding="latin-1")

letters = [x.upper() for x in sys.argv]
letters.pop(0)

letterword = "".join(letters)

for line in f:
    try:
        string = line.strip().upper()
        if len(string) <= len(letters) and len(string) > 2:
            possible = True
            for l in list(string):
                if l not in letters:
                    possible = False
                if string.count(l) > letterword.count(l):
                    possible = False
            if possible:
                print(string)
    except UnicodeDecodeError:
        pass
