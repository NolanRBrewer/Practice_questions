scrabble = open("scrabbleProblems/scrabble.txt","r")
line= scrabble.readline().strip()
while (line):
    if "B" in line and "X" in line and len(line)<=5:
        print(line)
    line= scrabble.readline().strip()