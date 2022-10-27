countries = open("countryproblems/countries.txt","r")
vowels = ["A","E","I","O","U"]
line = countries.readline().strip()
while (line):
    if line.startswith(tuple(vowels)) and line.upper().endswith(tuple(vowels)):
        print(line)
    line = countries.readline().strip()