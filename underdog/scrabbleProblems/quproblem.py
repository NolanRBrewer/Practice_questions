scrabble = open("scrabbleProblems/scrabble.txt","r")
line= scrabble.readline().strip()
while (line):
    if "Q" in line and not "U" in line:
        print(line)
    line= scrabble.readline().strip()