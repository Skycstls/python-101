import sys

width = int(sys.argv[1])
height = int(sys.argv[2])

chars = "┌┐└┘│─"

def createTop(length):
    return chars[0] + chars[5] * (length - 2) + chars[1]

def createBottom(length):
    return chars[2] + chars[5] * (length - 2) + chars[3]

def createMiddle(length):
    return chars[4] + " " * (length - 2) + chars[4]

def createBox(width, height):
    return createTop(width) + "\n" + (createMiddle(width) + "\n") * (height - 2) + createBottom(width)

print(createBox(width, height))