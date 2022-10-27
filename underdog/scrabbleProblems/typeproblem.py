scrabble = open("scrabble.txt","r")
line= scrabble.readline().strip()
count=0
while (line):
    if "TYPE" in line:
        count += 1
    line= scrabble.readline()
print(count).strip()