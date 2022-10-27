scrabble = open("scrabbleProblems/scrabble.txt","r")
line = scrabble.readline().strip()
while (line):
    line = scrabble.readline().strip()
    a_index = line.find("A")
    e_index = line.find("E")
    i_index = line.find("I")
    o_index = line.find("O")
    u_index = line.find("U")
    if a_index > -1 and a_index < e_index and e_index < i_index and i_index < o_index and o_index < u_index:
        print(line)