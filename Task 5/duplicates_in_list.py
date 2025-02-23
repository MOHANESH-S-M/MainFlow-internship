# This is Task 5
"""35. Find Duplicates in a List
 Objective    : Identify all duplicate elements in a list.
 Input        : A list of integers.
 Output       : A list of duplicate integers.
 Hint         : Use a dictionary or collections.Counter to count occurrences.""" 
def find_duplicates(a):
    list_dictionary ={}
    duplicates = []
    for i in a :
        if i in list_dictionary.keys():
            list_dictionary[i] += 1
        else :
            list_dictionary[i] = 1
    for k,v in list_dictionary.items():
        if v > 1 :
            duplicates.append(k)
    return duplicates
my_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,  # Unique values
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,  # Unique values
    2, 4, 6, 8, 10, 12, 14, 16, 18, 20,  # Duplicates from above
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30  # Unique values
]

print(find_duplicates(my_list))

