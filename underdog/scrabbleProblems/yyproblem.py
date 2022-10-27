scrabble = open("scrabble.txt","r")
line = scrabble.readline()
while (line):
    line = line.strip()
    if line.startswith("Y") and line.endswith("Y"):
        print(line)
    line = scrabble.readline()