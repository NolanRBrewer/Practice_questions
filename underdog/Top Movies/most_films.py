import csv

distributors = {}

with open("Top Movies/top_movies.csv") as top_movies:
    movie_reader = csv.reader(top_movies)
    next(movie_reader, None)
    for row in movie_reader:
        if row[1] not in distributors:
            distributors[row[1]] = 1
        else:
            distributors.update({row[1]: distributors[row[1]] + 1})
print(distributors)