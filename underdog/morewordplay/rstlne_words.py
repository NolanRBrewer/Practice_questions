words = [elt.strip() for elt in open("MoreSolutions/morewordplay/scrabble.txt","r").readlines()]


# valid_words = []

def set_compare(word):
    usable_letters = set("RSTLNE")
    set_diff = set(word).difference(usable_letters)
    return set_diff == set()
        
# for word in words:
#     set_diff = set(word).difference(usable_letters)
#     if set_diff == set():
#         valid_words.append(word)
    # if set(word) == usable_letters:
    #     valid_words.append(word)
    # # if len(set(word))
print(list(filter(set_compare, words)))