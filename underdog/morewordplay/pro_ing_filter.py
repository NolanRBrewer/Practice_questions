words = [elt.strip() for elt in open("MoreSolutions/morewordplay/scrabble.txt","r").readlines()]

def yes_pro(word):
    return word.startswith("PRO") and word.endswith("ING") and len(word) == 11

print(list(filter(yes_pro, words)))