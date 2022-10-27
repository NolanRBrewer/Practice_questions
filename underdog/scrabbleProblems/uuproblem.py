scrabble = open("scrabble.txt","r")
line= scrabble.readline().strip()
while (line):
    if "UU" in line:
        print(line)
    line= scrabble.readline().strip()