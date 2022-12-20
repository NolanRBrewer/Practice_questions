words = [elt.strip() for elt in open("MoreSolutions/morewordplay/scrabble.txt","r").readlines()]

unsorted_words = []
shortest_pro_words = []
for word in words:
    if word.startswith("PRO") and word.endswith("ING"):
        unsorted_words.append(word)

def Sorting(unsorted_words):
    unsorted_words.sort(key=len)
    return(unsorted_words)

sorted_words = (Sorting(unsorted_words))
print("Words should only be " + str(len(sorted_words[0])) + " letters long:")
for word in sorted_words:
    if len(word) == len(sorted_words[0]):
        shortest_pro_words.append(word)

print(shortest_pro_words)