# This is Task 7
""" 51. Longest Substring Without Repeating Characters
 Objective   : Given a string, find the length of the longest substring without repeating characters.
 Input       : A string.
Output       : The length of the longest substring without repeating characters.
 Hint        : Use the sliding window technique and a hash set or dictionary to track characters."""
def longest_unique_substring(s):
    char_index = {}
    left = max_length = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Example
print(longest_unique_substring("abcabcbb"))
