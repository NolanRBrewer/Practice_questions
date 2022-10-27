#Open file
baby_names = open("babynames/baby_names_2020_short.txt", "r")
scrabble = open("scrabbleProblems/scrabble.txt", "r")


for baby_name in baby_names:
    for scrabble_word in scrabble:
        if baby_name.strip().upper()[::-1] == scrabble_word.strip():
            print(baby_name)
    scrabble.seek(0)
       