# This is Task 5
"""33. Find All Permutations of a String
 Objective    : Generate all permutations of a given string.
 Input        : A string.
 Output       : List of all permutations.
 Hint         : Use recursion to swap characters or itertools.permutations."""
def permutation_of_string(word):
    if len(word) == 1 :
        return word
    perms = permutation_of_string(word[1:])
    char = word[0]
    result = []

    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result
print(permutation_of_string('abc'))