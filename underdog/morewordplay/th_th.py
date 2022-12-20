words = [elt.strip() for elt in open("scrabble.txt").readlines()]
contains_cat = [word for word in words if word.startswith("TH") and word.endswith("TH")]
print(contains_cat)