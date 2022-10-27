scrabble = open("scrabbleProblems/scrabble.txt","r")
line = scrabble.readline().strip()
while (line):
    if not "A" in line and not "E" in line  and not "I" in line and not "O" in line and not "U" in line and not "Y" in line:
        print(line)
    line = scrabble.readline().strip()