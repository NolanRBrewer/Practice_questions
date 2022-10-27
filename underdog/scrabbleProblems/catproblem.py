scrabble = open("scrabbleProblems/scrabble.txt","r")
line = scrabble.readline().strip()
while (line):
    if "CAT" in line and len(line)==6:
        print(line)
    line = scrabble.readline().strip()