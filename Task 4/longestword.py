# this is task 4
"""27. Longest Word in a Sentence
 Objective   : Find the longest word in a given sentence.
 Input       : A string (sentence).
 Output      : The longest word.
 Hint        : Split the string into words and compare lengths."""
def longest_word(sentence):
    sentence = sentence.strip()
    list_words = sentence.split(" ")
    max_word = ""
    for i in list_words:
       if len(max_word)<len(i):
          max_word = i
    return max_word
a = "  This is example program for the output verfication purposes"
print(longest_word(a))