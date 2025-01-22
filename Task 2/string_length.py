#this is task2 question no 15
"""15. String Length
 Objective     : Find the length of a string without using the len() function.
 Input         : A string.
 Output        : Integer representing the length.
 Hint          : Use a loop to count characters in the string."""
def string_length(s):
    count = 0
    for i in s:
        count+=1
    return count
print(string_length("This"))