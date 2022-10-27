scrabble = open("scrabbleProblems/scrabble.txt","r")
length = 0
word = ""
line = scrabble.readline().strip()
while (line):
    if line == line[::-1] and len(line) > length:
        word = line
        length = len(line)
    line = scrabble.readline().strip()
print(word)