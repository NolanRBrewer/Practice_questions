scrabble = open("scrabbleProblems/scrabble.txt","r")
list =[]
line = scrabble.readline().strip()
while (line):
    if line.endswith("GHTLY"):
        list.append(line)
    line = scrabble.readline().strip()
print(list)