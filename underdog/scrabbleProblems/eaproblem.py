scrabble = open("scrabbleProblems/scrabble.txt","r")
line= scrabble.readline().strip()
while (line):
    if not "E" in line and not "A" in line and len(line)>=16:
        print(line)
    line= scrabble.readline().strip()