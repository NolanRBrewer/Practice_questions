words = [elt.strip() for elt in open("MoreSolutions/morewordplay/scrabble.txt","r").readlines()]

not_allowed_letters = set("AEIO")
u_words = []
for word in words:
    if "U" in word and not_allowed_letters - set(word) == not_allowed_letters:
        u_words.append(word)
print(u_words)