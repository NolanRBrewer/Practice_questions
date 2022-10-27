scrabble = open("scrabbleProblems/scrabble.txt","r")
length = 20
word = ""
line = scrabble.readline().strip()
while (line):
    if "A" in line and "E" in line  and "I" in line and "O" in line and "U" in line and "Y" in line and len(line) < length:
        word = line
        length = len(line)
    line = scrabble.readline().strip()
print(word)