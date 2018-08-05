#!/usr/bin/env python3
# 13.8 -- MARKOV ANALYSIS

import argparse, string, sys, random


def stripper(longstring):
    splitString = longstring.split("\n")

    longstring = " ".join(splitString)

    omission = "_()<>/"
    table = str.maketrans(omission, " " * len(omission))
    theString = string.whitespace + string.punctuation
    wordList = longstring.strip(theString).translate(table).split()

    return wordList # @returns a list of all words in the file

def markov(wordList, characters, pLength=3):

    dicInst = {}

    for i in range(len(wordList) - pLength):
        prefix = ""
        index = 0

        for j in range(i, i + pLength):
            prefix += wordList[j] + " "
            index = j

        suffix = wordList[index + 1]

        if prefix not in dicInst:
            dicInst[prefix] = [suffix]
        else:
            dicInst[prefix].append(suffix)

    # Pick a random prefix
    prefix = random.choice(list(dicInst.keys()))

    # Print once beforehand
    print(prefix, end="")

    while True:
        newfix = ""
        splitted = prefix.split() # for creating newfix

        for i in range(1, pLength):
            newfix += splitted[i] + " "

        try:
            rand = random.choice(dicInst[prefix])
        except KeyError:
            print("\n\n\nTHE END")
            return

        if rand in characters:
            print()
            print()
        print(rand, end=" ")

        newfix += rand + " "

        prefix = newfix



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="target file", type=str)
    parser.add_argument("characters", help="list of characters", type=str)
    args = parser.parse_args()

    f = open(args.target)
    charList = []
    characters = open(args.characters).read().split("\n")

    for char in characters:
        charList.append(char)

    stripList = stripper(f.read())

    markov(stripList, charList)
