def count_vowels(string):
    xcount = 0
    for letter in string.upper():
        if letter in vowels:
            xcount += 1
    return xcount
def count_consonants(string):
    ycount =0
    for letter in string.upper():
        if letter not in vowels:
            ycount += 1
    return ycount

countries = open("countryproblems/countries.txt","r")
vowels = ["A","E","I","O","U"]
line = countries.readline().strip()
while (line):
    if count_vowels(line) > count_consonants(line):
        print(line)
    line = countries.readline().strip()