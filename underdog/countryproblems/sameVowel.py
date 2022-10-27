countries = open("countryproblems/countries.txt","r")
vowels = set("AEIOU")
line = countries.readline().strip()
while (line):
    if len(set(line.upper()) & vowels) == 1:
        print(line)        
    line = countries.readline().strip()