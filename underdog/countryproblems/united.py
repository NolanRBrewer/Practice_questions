countries = open("countryproblems/countries.txt","r")
line = countries.readline().strip()
while (line):
    if "United" in line:
        print(line)
    line = countries.readline().strip()