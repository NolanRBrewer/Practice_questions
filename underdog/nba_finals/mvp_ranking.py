import csv
mvps = {}

with open('nba_finals/nba_finals.csv') as csvfile:
    nba_reader = csv.reader(csvfile)
    next(nba_reader, None)
    for row in nba_reader:
        mvp = row[4]
        if mvp == "":
            continue
        if mvp not in mvps:
            mvps[mvp] = 1
        else:
            mvps.update({mvp: mvps[mvp] + 1})
mvp_ranking = dict(sorted(mvps.items(), key = lambda item: item[1], reverse = True))
for item in mvp_ranking.items():
    print(f'{item[1]} times: {item[0]}')