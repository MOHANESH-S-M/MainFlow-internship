#this is task 2 question no 16
""" 16. Count Vowels and Consonants
 Objective   : Count the number of vowels and consonants in a string.
 Input       : A string.
 Output      : Two integers: count of vowels and count of consonants.
 Hint        : Define a set of vowels ('a', 'e', 'i', 'o', 'u'), and use string methods to identify letters"""
def count_vo_cons(s):
    count_v =0
    count_c =0
    for i in s:
        if i.lower() in ('a', 'e', 'i', 'o', 'u'):
            count_v+=1
        elif i.isalpha():
            count_c+=1
    return f"Count of Vowels: {count_v}, Count of Consonants: {count_c}"
print(count_vo_cons("this is a string"))