words = [elt.strip() for elt in open("MoreSolutions/morewordplay/scrabble.txt","r").readlines()]

pro_words = []
 
for word in words:
    if word.startswith("PRO") and word.endswith("ING") and len(word) == 11:
        pro_words.append(word)

print(pro_words)