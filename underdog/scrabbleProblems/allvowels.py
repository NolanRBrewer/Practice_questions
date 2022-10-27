scrabble = open("scrabbleProblems/scrabble.txt","r")
line = scrabble.readline().strip()
while (line):
    if "A" in line and "E" in line  and "I" in line and "O" in line and "U" in line and "Y" in line:
        print(line)
    line = scrabble.readline().strip()