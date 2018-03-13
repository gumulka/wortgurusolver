#!/usr/bin/python3

import sys

f = open("german.dic", "r", encoding="latin-1")

args = sys.argv

args.pop(0)

letters = []
number = 2
for x in sys.argv:
    try:
        number = int(x)
    except ValueError:
        if len(x) == 1:
            letters.append(x.upper())
        else:
            for l in list(x):
                letters.append(l.upper())

letterword = "".join(letters)


for line in f:
    try:
        string = line.strip().upper()
        if len(string) <= len(letters) and len(string) >= number:
            possible = True
            for l in list(string):
                if l not in letters:
                    possible = False
                    break;
                if string.count(l) > letterword.count(l):
                    possible = False
                    break;
            if possible:
                print(string)
    except UnicodeDecodeError:
        pass
