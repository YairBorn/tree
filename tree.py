from genericpath import isdir
import os
import sys


def printTree(path, indentLevel, firstLevel=False):
    onlyFolders = [f for f in os.listdir(path) if (isdir(path + "\\" + f) and not f.startswith(".")) ]

    count = 0
    for folder in onlyFolders:
        count += 1
        lineStarter = "└"  if len(onlyFolders) == count else "├"
        print("│" if not firstLevel else "", end="")
        if indentLevel > 1: print(" " * (indentLevel -1), end="")
        print("   "*indentLevel  + lineStarter+ "───" + folder)
        printTree(path + "\\" + folder, indentLevel+1)

def main(argv):
    printTree("C:\\Users\\YairPC\\Documents", 0, True)


if __name__ == "__main__":
    main(sys.argv)
