#this is task 3 question 19
""" 19. Check Substring
 Objective  : Determine if one string is a substring of another.
 Input      : Two strings s1s1s1 (main string) and s2s2s2 (substring).
 Output     : True if s2s2s2 is a substring of s1s1s1, otherwise False.
 Hint       : Use Python's in operator or string slicing to search for substrings."""
def check_substrig(main_str,sub_str):
    if sub_str in main_str:
        return True
    return False
print(check_substrig("aabbddhrdbbssssjejdnnnnjjkihh","je"))