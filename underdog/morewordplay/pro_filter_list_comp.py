words = [word.strip() for word in open("MoreSolutions/morewordplay/scrabble.txt","r").readlines()]
words = [word for word in words if word.startswith("PRO") and word.endswith("ING") and len(word) == 11]
print(words)