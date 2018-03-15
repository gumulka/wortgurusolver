#!/usr/bin/python3

import sys

f = open("german.small", "r")

args = sys.argv

args.pop(0)

letters = []
minimal = -1
maximal = 100
for x in sys.argv:
    try:
        if minimal == -1:
            minimal = int(x)
        else:
            maximal = int(x)
    except ValueError:
        if len(x) == 1:
            letters.append(x.upper())
        else:
            for l in list(x):
                letters.append(l.upper())

letterword = "".join(letters)

if len(letters) == 0:
    print("You must pass the available letters as arguments.")
    print("A number can be passed to indicate the minimal size of words")
    exit(-1)


for line in f:
    string = line.strip().upper()
    length = len(string)
    if length <= len(letters) and length >= minimal and length <= maximal:
        possible = True
        for l in list(string):
            if l not in letters:
                possible = False
                break
            if string.count(l) > letterword.count(l):
                possible = False
                break
        if possible:
            print(line.strip())
