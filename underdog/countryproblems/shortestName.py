import math
countries = open("countryproblems/countries.txt","r")
line = countries.readline().strip()
length = math.inf
countries_list = []
while (line):
    if len(line) < length:
        countries_list = [line]
        length = len(line)
    elif len(line) == length:
        countries_list.append(line)
    line = countries.readline().strip()
print(countries_list)