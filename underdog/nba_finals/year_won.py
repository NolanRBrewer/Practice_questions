import csv

def winner(team):
    years_won = []
    
    with open('nba_finals/nba_finals.csv') as csvfile:
        nba_reader = csv.reader(csvfile)
        for row in nba_reader:
            year_column = row[0]
            team_column = row[1]
            if team_column == team:
                years_won.append(year_column)
            
        return years_won
        
            
answer = input("Pick a team: ")
print(winner(answer))