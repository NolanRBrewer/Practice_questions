words = [elt.strip() for elt in open("MoreSolutions/morewordplay/scrabble.txt","r").readlines()]
# takes list of words and returns only ones that can be made from letters "RSTLNE"
def good_words(word):
    usable_letters = set("RSTLNE")
    set_diff = set(word).difference(usable_letters)
    return set_diff == set()
# sorts list of usable words by length shortest to longest
def sorting(unsorted_words):
    unsorted_words.sort(key=len)
    return(unsorted_words)

rstlne_words = list(filter(good_words, words))

shortest_to_longest = sorting(rstlne_words)
longest_to_shortest = shortest_to_longest[::-1]
# displays longest word and any ties
for word in longest_to_shortest:
    if len(word) == len(longest_to_shortest[0]):
        print(word)