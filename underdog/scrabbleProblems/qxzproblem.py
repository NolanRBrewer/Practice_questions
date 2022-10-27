scrabble = open("scrabbleProblems/scrabble.txt","r")
qcount = 0
xcount = 0
zcount = 0
line = scrabble.readline().strip()
while (line):
    qcount += line.count("Q") 
    xcount += line.count("X")
    zcount += line.count("Z")
    line= scrabble.readline().strip()
if qcount < xcount and qcount < zcount:
    print("Q count:" + str(qcount))
elif xcount < qcount and xcount < zcount:
    print("X count:" + str(xcount))
elif zcount < qcount and zcount < xcount:
    print("Z count:" + str(zcount)) 