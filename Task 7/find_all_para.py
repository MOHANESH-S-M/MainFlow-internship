# This is Task 7
"""52. Find All Valid Parentheses Combinations
 Objective   : Generate all possible valid combinations of parentheses.
 Input       : An integer nnn, representing the number of pairs of parentheses.
 Output      : A list of valid parentheses combinations.
 Hint        : Use recursion and backtracking to generate valid combinations."""
def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)

    result = []
    backtrack("", 0, 0)
    return result

# Example
print(generate_parentheses(3))
