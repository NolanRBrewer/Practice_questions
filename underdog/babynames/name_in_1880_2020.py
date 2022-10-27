#reading file
names_of_1880 = open("babynames/baby_names_1880_short.txt","r")
names_of_2020 = open("babynames/baby_names_2020_short.txt","r")

#searching for names
for name_1880 in names_of_1880:
    for name_2020 in names_of_2020:
        if name_1880.strip().upper() == name_2020.strip().upper():
            print(name_1880)
    names_of_2020.seek(0)