import math

baby_names = open("babynames/baby_names_2020_short.txt","r")
length = math.inf
names_list = []
line = baby_names.readline().strip()
while (line):
    if len(line) < length:
        names_list = [line]
        length = len(line)
    elif len(line) == length:
        names_list.append(line)
    line = baby_names.readline().strip()
print(names_list)