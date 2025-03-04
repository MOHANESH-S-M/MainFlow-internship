# This is Task 6
""" 40. Word Frequency in Text
 Objective    : Count the frequency of each word in a given text.
 Input        : A string of text.
 Output       : A dictionary where keys are words and values are their counts.
 Hint         : Use split() to separate words and a dictionary to store counts"""
def word_frequency(text):
    words_dict = {}
    words = text.split(" ")
    for i in words:
        if i in list(words_dict.keys()):
            words_dict[i] += 1
        else:
            words_dict[i] = 1
    return words_dict
print(word_frequency("The sun rises in the east and sets in the west. The sun is bright"
))

    