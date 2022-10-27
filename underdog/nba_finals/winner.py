import csv

def winner(year):
    with open('nba_finals/nba_finals.csv') as csvfile:
        nba_reader = csv.reader(csvfile)
        for row in nba_reader:
            if row[0] == year:
                return row[1]
            
answer = input("Pick a year: ")
print(winner(answer))