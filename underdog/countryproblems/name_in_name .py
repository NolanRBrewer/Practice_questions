# reading file
countries_file = open("countryproblems/countries.txt","r")
countries_file_2 = open("countryproblems/countries.txt","r")

for country in countries_file:
    for country_2 in countries_file_2:
        if country.strip().upper() in country_2.strip().upper() and country != country_2:
             print(country)
             print(country_2)
    countries_file_2.seek(0)