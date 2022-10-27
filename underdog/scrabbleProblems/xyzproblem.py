scrabble = open("scrabble.txt","r")
line= scrabble.readline().strip()
while (line):
    if "X" in line and "Y" in line and "Z" in line:
        print(line)
    line= scrabble.readline().strip()