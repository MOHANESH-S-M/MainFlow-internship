# This is Task 7
"""48. Find the Longest Palindromic Substring
 Objective    : Find the longest palindromic substring in a given string.
 Input        : A string.
 Output       : The longest palindromic substring.
 Hint         : Use dynamic programming or expand around center approach."""
def longest_palindromic_substring(s):
    if not s:
        return ""

    start, max_length = 0, 0

    def expand_around_center(left, right):
        nonlocal start, max_length
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_length:
                start, max_length = left, right - left + 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)      # Odd-length palindrome
        expand_around_center(i, i + 1)  # Even-length palindrome

    return s[start:start + max_length]

# Example
print(longest_palindromic_substring("babad"))
