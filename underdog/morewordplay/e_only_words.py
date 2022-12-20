words = [elt.strip() for elt in open("MoreSolutions/morewordplay/scrabble.txt","r").readlines()]

not_allowed = set("AIOU")
e_words = []

for word in words:
    if "E" in word and not_allowed - set(word) == not_allowed and len(word) >= 15:
        e_words.append(word)
print(e_words)