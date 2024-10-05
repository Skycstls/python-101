import sys

width = int(sys.argv[1])
height = int(sys.argv[2])

chars_simple = "┌┐└┘│─"
chars_double = "╔╗╚╝║═"

chars = chars_double

def createLine(start, mid, end, length):
    return start + mid * (length - 2) + end

def createBox(width, height):
    top = createLine(chars[0], chars[5], chars[1], width)
    middle = createLine(chars[4], " ", chars[4], width)
    bottom = createLine(chars[2], chars[5], chars[3], width)
    return top + "\n" + (middle + "\n") * (height - 2) + bottom

print(createBox(width, height))