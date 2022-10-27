scrabble = open("scrabbleProblems/scrabble.txt","r")
list = ["AA","BB","CC","DD","EE","FF","GG","HH","II","JJ","KK","LL","MM","NN","OO","PP","QQ","RR","SS","TT","UU","VV","WW","XX","YY","ZZ"]
match_list = []
unused = []
line = scrabble.readline().strip()
while (line):
    for substring in list:
        if substring in line and substring not in match_list:
            match_list.append(substring)
    line = scrabble.readline().strip()
for i in list:
    if i not in match_list:
        unused.append(i)
print(unused)