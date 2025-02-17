# This is Task 4
"""28. Count Words in a Sentence
 Objective  : Count the number of words in a sentence.
 Input      : A string (sentence).
 Output     : Integer representing the word count.
 Hint       : Use the split() method to divide the string by spaces and count elements."""
def count_words(s):
    s= s.strip()
    list_words = s.split(" ")
    return len(list_words)
a = " This is example program for the output verfication purposes"
print(count_words(a))