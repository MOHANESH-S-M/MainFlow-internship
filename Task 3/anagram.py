#this is task 3
""" 24. Check Anagram
 Objective   : Check if two strings are anagrams (contain the same characters in any order).
 Input       : Two strings.
 Output      : True if anagrams, otherwise False.
 Hint        : Use sorted() on both strings or count character occurrences using a dictionary."""
def is_anagram(str1,str2):
    if len(str1)!= len(str2):
        return False
    char_count_str1 ={}
    char_count_str2 ={}
    for ch in str1:
        char_count_str1[ch] = char_count_str1.get(ch,0)+1
    for ch in str2:
        char_count_str2[ch] = char_count_str2.get(ch,0)+1
    return char_count_str2 == char_count_str1
print(is_anagram("abccd","dccba"))